import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import pyzed.sl as sl
import cv2
import math
from threading import Thread

from new_detect import Aruco, Orange, Bottle  # Object detection modules

class ZEDPublisher(Node):
    def __init__(self):
        super().__init__('zed_publisher')
        self.publisher_ = self.create_publisher(String, 'zed_data', 10)
        self.zed = sl.Camera()
        self.detect_type = 2

        # ZED Initialization
        init_params = sl.InitParameters()
        init_params.depth_mode = sl.DEPTH_MODE.ULTRA
        init_params.coordinate_units = sl.UNIT.MILLIMETER

        if self.zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
            self.get_logger().error("Failed to open ZED camera")
            exit()

        self.runtime_parameters = sl.RuntimeParameters()
        self.image = sl.Mat()
        self.point_cloud = sl.Mat()

        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        while rclpy.ok():
            if self.zed.grab(self.runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                self.zed.retrieve_image(self.image, sl.VIEW.LEFT)
                image_ocv = self.image.get_data()

                # Object Detection
                if self.detect_type == 0:
                    processed_image, x, y = Bottle().bottle_detect(image_ocv)
                elif self.detect_type == 1:
                    processed_image, x, y = Aruco().aruco_detect(image_ocv)
                else:
                    processed_image, x, y = Orange().orange_detect(image_ocv)

                # Distance Calculation
                if x and y:
                    err, point_cloud_value = self.point_cloud.get_value(x, y)
                    if math.isfinite(point_cloud_value[2]):
                        distance = math.sqrt(sum(p**2 for p in point_cloud_value[:3]))
                        msg = f"X: {x}, Y: {y}, Distance: {distance:.2f} mm"
                        self.publisher_.publish(String(data=msg))
                        self.get_logger().info(f"Published: {msg}")

    def destroy_node(self):
        super().destroy_node()
        self.zed.close()


def main():
    rclpy.init()
    node = ZEDPublisher()
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
