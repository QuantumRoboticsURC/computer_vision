import asyncio
import websockets
import cv2
import base64
import pyzed.sl as sl
import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
from custom_interfaces.msg import CA  # Ensure the correct message type is used
from .submodules.new_detect import Aruco, Orange, Bottle

stop_server = False
detect_type = 2  # Default to Orange

zed = sl.Camera()

# Initialize ZED Camera
init_params = sl.InitParameters()
init_params.depth_mode = sl.DEPTH_MODE.ULTRA
init_params.coordinate_units = sl.UNIT.MILLIMETER
status = zed.open(init_params)

if status != sl.ERROR_CODE.SUCCESS:
    print("Camera Open Error:", repr(status))
    exit()

runtime_parameters = sl.RuntimeParameters()
image = sl.Mat()
depth = sl.Mat()
point_cloud = sl.Mat()
mirror_ref = sl.Transform()
mirror_ref.set_translation(sl.Translation(2.75, 4.0, 0))

x, y = 360, 360


class ROS2Detection(Node):
    def __init__(self):
        super().__init__("ros2_detection")
        self.subscription = self.create_subscription(Int8, "/detection_target", self.target_callback, 10)
        self.publisher = self.create_publisher(CA, "/detection_result", 10)
        self.get_logger().info("ROS2 Detection Node Initialized")

    def target_callback(self, msg):
        """Updates detection type based on user input."""
        global detect_type
        detect_type = msg.data
        self.get_logger().info(f"Detection type updated to {detect_type}")

    def publish_detection(self, x, y, distance):
        """Publishes detection results."""
        msg = CA()
        msg.x = x
        msg.y = y
        msg.distance = distance
        msg.detected = True if x is not None and y is not None else False
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: x={x}, y={y}, distance={distance}")


ros_node = None


async def video_stream(websocket):
    global stop_server, ros_node
    try:
        while not stop_server:
            if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                # Retrieve left image
                zed.retrieve_image(image, sl.VIEW.LEFT)
                image_ocv = image.get_data()

                # Retrieve point cloud
                zed.retrieve_measure(point_cloud, sl.MEASURE.XYZRGBA)

                if detect_type == 0:
                    processed_image, x, y = Bottle().bottle_detect(cv2.cvtColor(image_ocv, cv2.COLOR_BGRA2RGB))
                elif detect_type == 1:
                    processed_image, x, y = Aruco().aruco_detect(image_ocv)
                else:
                    processed_image, x, y = Orange().orange_detect(image_ocv)

                print(f"Detection: x={x}, y={y}")

                distance = None
                if x is not None and y is not None:
                    err, point_cloud_value = point_cloud.get_value(x, y)
                    if math.isfinite(point_cloud_value[2]):
                        distance = math.sqrt(point_cloud_value[0]**2 + point_cloud_value[1]**2 + point_cloud_value[2]**2)
                        print(f"Distance: {distance}")

                # Publish detection data to ROS2
                if ros_node:
                    ros_node.publish_detection(x, y, distance)

                # Encode image for streaming
                _, buffer = cv2.imencode('.jpg', processed_image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
                frame_data = base64.b64encode(buffer).decode('utf-8')
                await websocket.send(frame_data)

                await asyncio.sleep(0.01)

    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")
        stop_server = True
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Video capture released.")


async def main():
    global ros_node
    rclpy.init()
    ros_node = ROS2Detection()

    server = await websockets.serve(video_stream, '192.168.0.16', 9999, ping_interval=None)

    try:
        rclpy.spin(ros_node)
        await server.wait_closed()
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        loop.run_forever()
    except KeyboardInterrupt:
        print("Server interrupted by user.")
    finally:
        loop.run_until_complete(asyncio.sleep(0.1))
        loop.close()
        print("Event loop closed. Program exited.")
