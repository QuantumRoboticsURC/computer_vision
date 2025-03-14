import asyncio
import websockets
import cv2
import base64
import pyzed.sl as sl
import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8,Bool
from custom_interfaces.msg import CA  # Ensure the correct message type is used
from new_detect import Aruco, Orange, Bottle

from rclpy.executors import SingleThreadedExecutor, MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup

class ZED_NODE(Node):
	
	def __init__(self):
		super().__init__('zed_node')
		server_group = MutuallyExclusiveCallbackGroup()
		publisher_group = ReentrantCallbackGroup()
		async_group = MutuallyExclusiveCallbackGroup()
		self.zed = sl.Camera()

		# Initialize ZED Camera
		self.init_params = sl.InitParameters()
		self.init_params.depth_mode = sl.DEPTH_MODE.ULTRA
		self.init_params.coordinate_units = sl.UNIT.MILLIMETER
		status = self.zed.open(self.init_params)
		if status != sl.ERROR_CODE.SUCCESS:
			print("Camera Open Error:", repr(status))
			exit()

		self.runtime_parameters = sl.RuntimeParameters()
		self.image = sl.Mat()
		self.depth = sl.Mat()
		self.point_cloud = sl.Mat()
		self.mirror_ref = sl.Transform()
		self.mirror_ref.set_translation(sl.Translation(2.75, 4.0, 0))
		self.ip = '192.168.0.16'
		self.port = 9888
		self.CA = CA()
		self.x, self.y,self.distance = None, None,0
		self.detect_type = 1  # Default to Aruco
		self.frame_data = None
		self.x_zed = round(self.image.get_width() / 2)
		self.y_zed = round(self.image.get_height() / 2)
		self.create_subscription(Int8, "/state", self.target_callback, 1,callback_group=publisher_group)
  
		self.publisher = self.create_publisher(CA, "/center_approach", 10)	
		self.aruco = self.create_publisher(Bool, "/detected_aruco", 1)
		self.orange = self.create_publisher(Bool, "/detected_orange", 1)
		self.bottle = self.create_publisher(Bool, "/detected_bottle", 1)
		self.detected = Bool()
		
  
		self.server = self.create_timer(0.01,self.zed_server,callback_group=server_group)
		self.async_server = self.create_timer(0.01,self.zed_async_server,callback_group=async_group)
		self.publisher_timer = self.create_timer(0.01,self.publish_detection,callback_group=publisher_group)

	def between(self,val,minus,plus):
		if not val:
			return False
		if val>minus and val<plus:
			return True
		return False

	def publish_detection(self):
		if self.x is None or self.y is None:
			self.CA.detected = False
			self.CA.x = 0  # Default value
			self.CA.distance = 0.0  # Default value
			self.detected.data = False
			if self.detect_type == 1: 
				self.aruco.publish(self.detected)
			elif self.detect_type == 2:
				self.orange.publish(self.detected)
			else:
				self.bottle.publish(self.detected)
			
		else:
			
			self.CA.x = self.x - self.x_zed
			self.CA.distance = self.distance
			self.CA.detected = True if self.x is not None else False #self.between(self.x,self.x_zed-80,self.x_zed+80)
			if self.detect_type == 2: #Bottle
				self.detected.data = True
				self.bottle.publish(self.detected)
				self.detected.data = False
				self.aruco.publish(self.detected)
				self.orange.publish(self.detected)
			elif self.detect_type == 4: #|Aruco
				self.detected.data = True
				self.aruco.publish(self.detected)
				self.detected.data = False
				self.bottle.publish(self.detected)
				self.orange.publish(self.detected)
			elif self.detect_type == 3: # Orange
				self.detected.data = True
				self.orange.publish(self.detected)
				self.detected.data = False
				self.aruco.publish(self.detected)
				self.bottle.publish(self.detected)
			else:
				self.detected.data = False
				self.aruco.publish(self.detected)
				self.orange.publish(self.detected)
				self.bottle.publish(self.detected)

		self.publisher.publish(self.CA)

	def target_callback(self, msg):
		self.detect_type = msg.data

	def zed_server(self):
		try:
			if self.zed.grab(self.runtime_parameters) == sl.ERROR_CODE.SUCCESS:
				# Retrieve left image
				self.zed.retrieve_image(self.image, sl.VIEW.LEFT)
				image_ocv = self.image.get_data()
				self.x_zed = round(self.image.get_width() / 2)
				self.y_zed = round(self.image.get_height() / 2)
				depth_ocv = self.depth.get_data()
				# Retrieve colored point cloud. Point cloud is aligned on the left image.
				self.zed.retrieve_measure(self.point_cloud, sl.MEASURE.XYZRGBA)
				# Convert image_ocv from BGRA to RGB for processing
				
				if self.detect_type ==0:
					# Detect bottles using YOLO model
					image_rgb = cv2.cvtColor(image_ocv, cv2.COLOR_BGRA2RGB)
					processed_image, x, y = Bottle().bottle_detect(image_rgb)
					print(f"Bottle at {x},{y}")
				elif self.detect_type==1:
				# Detect Aruco markers
					processed_image, x, y = Aruco().aruco_detect(image_ocv)
					print(f"AR at {x},{y}")
				else:
				# Detect oranges
					processed_image,x,y = Orange().orange_detect(image_ocv)
					print(f"oRANGE at {x},{y}")
				# Convert the processed image back to RGB for visualization (if needed)
				frame = processed_image#cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)

				# Compress the frame for streaming
				_, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
				self.frame_data = base64.b64encode(buffer).decode('utf-8')
				self.x = x
				self.y = y
				if x and y:
					err, point_cloud_value = self.point_cloud.get_value(x, y)

					if math.isfinite(point_cloud_value[2]):
						self.distance = math.sqrt(point_cloud_value[0] * point_cloud_value[0] +
									point_cloud_value[1] * point_cloud_value[1] +
									point_cloud_value[2] * point_cloud_value[2])
						print(f"Distance to Camera at {{{x};{y}}}: {self.distance}")
						
					else : 
						print(f"The distance can not be computed at {{{x},{y}}}")
						self.distance = float("inf")
		except Exception as e:
			self.get_logger().info(f"Error in zed_server: {e}")


	async def video_stream(self, websocket):
		try:
			while True:
				if self.frame_data:  # Ensure data exists
					await websocket.send(self.frame_data)
				else:
					print("No frame data available, sending empty frame")
					await websocket.send("")  # Send an empty frame instead of breaking
				await asyncio.sleep(0.05)  # Reduce delay for smoother streaming
		except websockets.exceptions.ConnectionClosed as e:
			print(f"Client disconnected: {e}")
		except Exception as e:
			print(f"WebSocket error: {e}")



	def zed_async_server(self):
		async def main():
			server = await websockets.serve(self.video_stream, self.ip, self.port, ping_interval=None)
			while True:
				await asyncio.sleep(1)

		# ✅ Fix: Explicitly create and set a new event loop in this thread
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)

		try:
			loop.run_until_complete(main())
			loop.run_forever()
		except KeyboardInterrupt:
			print("Server interrupted by user.")
		finally:
			loop.run_until_complete(asyncio.sleep(0.1))  # Allow tasks to settle
			loop.close()
			print("Event loop closed. Program exited.")	


def main(args=None):
	rclpy.init(args=args)
	zed = ZED_NODE()
	executor = MultiThreadedExecutor()
	executor.add_node(zed)
	executor.spin()
	zed.destroy_node()
	rclpy.shutdown()
	
if __name__=="__main__":
	main()
