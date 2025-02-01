import asyncio
import websockets
import cv2
import base64
import pyzed.sl as sl
from new_detect import Aruco, Orange, Bottle
import math

class ZEDWebSocketServer:
    def __init__(self, host='192.168.0.16', port=9999):
        self.host = host
        self.port = port
        self.zed = sl.Camera()
        self.detect_type = 2

        # ZED Initialization
        init_params = sl.InitParameters()
        init_params.depth_mode = sl.DEPTH_MODE.ULTRA
        init_params.coordinate_units = sl.UNIT.MILLIMETER

        if self.zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
            print("Failed to open ZED camera")
            exit()

        self.runtime_parameters = sl.RuntimeParameters()
        self.image = sl.Mat()

    async def video_stream(self, websocket, path):
        while True:
            if self.zed.grab(self.runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                self.zed.retrieve_image(self.image, sl.VIEW.LEFT)
                image_ocv = self.image.get_data()

                if self.detect_type == 0:
                    processed_image, _, _ = Bottle().bottle_detect(image_ocv)
                elif self.detect_type == 1:
                    processed_image, _, _ = Aruco().aruco_detect(image_ocv)
                else:
                    processed_image, _, _ = Orange().orange_detect(image_ocv)

                # Compress and encode the frame
                _, buffer = cv2.imencode('.jpg', processed_image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
                frame_data = base64.b64encode(buffer).decode('utf-8')

                await websocket.send(frame_data)
                await asyncio.sleep(0.01)  # Adjust delay as needed

    def start(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        server = websockets.serve(self.video_stream, self.host, self.port, ping_interval=None)
        loop.run_until_complete(server)
        loop.run_forever()


if __name__ == '__main__':
    server = ZEDWebSocketServer()
    server.start()
