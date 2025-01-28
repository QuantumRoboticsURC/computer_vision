import asyncio
import websockets
import cv2
import base64

from new_detect import Aruco,Orange,Bottle

stop_server = False

async def video_stream(websocket):
    global stop_server
    try:
        vid = cv2.VideoCapture(0)
        while vid.isOpened() and not stop_server:
            _, frame = vid.read()
            #frame,x,y = Orange().orange_detect(frame)
            frame,x,y = Aruco().aruco_detect(frame)
            #frame,x,y = Bottle().bottle_detect(frame)
            print(x,y)
            # Compress the frame
            _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            frame_data = base64.b64encode(buffer).decode('utf-8')
            await websocket.send(frame_data)
            await asyncio.sleep(0.1)  # Adjust the delay as needed
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")
        stop_server = True
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        vid.release()
        print("Video capture released.")

async def main():
    global stop_server
    server = await websockets.serve(video_stream, '192.168.0.59', 9999, ping_interval=None)

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
