
import asyncio
import websockets
import cv2
import base64
import pyzed.sl as sl
from new_detect import Aruco,Orange,Bottle

stop_server = False

zed = sl.Camera()

# Create a InitParameters object and set configuration parameters
init_params = sl.InitParameters()
init_params.depth_mode = sl.DEPTH_MODE.ULTRA  # Use ULTRA depth mode
init_params.coordinate_units = sl.UNIT.MILLIMETER  # Use meter units (for depth measurements)

# Open the camera
status = zed.open(init_params)
if status != sl.ERROR_CODE.SUCCESS: #Ensure the camera has opened succesfully
	print("Camera Open : "+repr(status)+". Exit program.")
	exit()

# Create and set RuntimeParameters after opening the camera
runtime_parameters = sl.RuntimeParameters()

i = 0
image = sl.Mat()
depth = sl.Mat()
point_cloud = sl.Mat()
image_ocv = image.get_data()
depth_ocv = image.get_data()
mirror_ref = sl.Transform()
mirror_ref.set_translation(sl.Translation(2.75,4.0,0))



async def video_stream(websocket):
    global stop_server
    try:
        while not stop_server:
            if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                # Retrieve left image
                zed.retrieve_image(image, sl.VIEW.LEFT)
                image_ocv = image.get_data()
                
                # Convert image_ocv from BGRA to RGB for processing
                image_rgb = cv2.cvtColor(image_ocv, cv2.COLOR_BGRA2RGB)

                # Detect bottles using YOLO model
                processed_image, x, y = Bottle().bottle_detect(image_rgb)
                # Detect Aruco markers
                #processed_image = Aruco().aruco_detect(image_ocv)
                # Detect oranges
                #processed_image = Orange().orange_detect(image_ocv)
                # Convert the processed image back to RGB for visualization (if needed)
                frame = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)

                # Compress the frame for streaming
                _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
                frame_data = base64.b64encode(buffer).decode('utf-8')

                # Send the frame data over the WebSocket
                await websocket.send(frame_data)
                await asyncio.sleep(0.1)  # Adjust the delay as needed
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")
        stop_server = True
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Video capture released.")

async def main():
    global stop_server
    server = await websockets.serve(video_stream, '192.168.0.16', 9999, ping_interval=None)

    try:
        await server.wait_closed()
    finally:
        # Cancel all tasks on shutdown
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        [task.cancel() for task in tasks]
        await asyncio.gather(*tasks, return_exceptions=True)
        print("Server and tasks shut down cleanly.")

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
    loop.run_forever()
except KeyboardInterrupt:
    print("Server interrupted by user.")
finally:
    loop.run_until_complete(asyncio.sleep(0.1))  # Allow tasks to settle
    loop.close()
    print("Event loop closed. Program exited.")
