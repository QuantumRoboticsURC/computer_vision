import numpy as np
import cv2
import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from custom_interfaces.msg import CA
from ultralytics import YOLO


class DetectionNode(Node):
    def __init__(self, topic_name, detection_class):
        super().__init__("detection_node")
        self.publisher = self.create_publisher(CA, "/detection_result", 10)
        self.status_publisher = self.create_publisher(Bool, topic_name, 10)
        self.detection_class = detection_class()
        self.get_logger().info(f"Initialized ROS2 publisher for {topic_name}")

    def publish_detection(self, x, y, distance):
        """Publishes detection data to the ROS2 topic."""
        msg = CA()
        msg.x = x if x is not None else 0.0
        msg.y = y if y is not None else 0.0
        msg.distance = distance if distance is not None else -1.0
        msg.detected = True if x is not None and y is not None else False
        self.publisher.publish(msg)

        status_msg = Bool()
        status_msg.data = msg.detected
        self.status_publisher.publish(status_msg)

        self.get_logger().info(f"Published Detection: x={msg.x}, y={msg.y}, distance={msg.distance}, detected={msg.detected}")


class Aruco(DetectionNode):
    def __init__(self):
        super().__init__("/detected_aruco", ArucoDetection)
        

class ArucoDetection:
    """Aruco detection class that processes frames."""
    def __init__(self):
        self.arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
        self.arucoParams = cv2.aruco.DetectorParameters()

    def aruco_detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, _ = cv2.aruco.detectMarkers(image=gray, dictionary=self.arucoDict, parameters=self.arucoParams)

        if len(corners) > 0:
            x, y = int(corners[0][0][0][0]), int(corners[0][0][0][1])
            return frame, x, y
        return frame, None, None


class Orange(DetectionNode):
    def __init__(self):
        super().__init__("/detected_orange", OrangeDetection)


class OrangeDetection:
    """Orange detection class using color thresholding."""
    def __init__(self):
        self.lower_orange = np.array([5, 130, 160])
        self.upper_orange = np.array([22, 255, 255])

    def orange_detect(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_orange, self.upper_orange)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            x, y, w, h = cv2.boundingRect(contours[0])
            return frame, x + w // 2, y + h // 2
        return frame, None, None


class Bottle(DetectionNode):
    def __init__(self):
        super().__init__("/detected_bottle", BottleDetection)


class BottleDetection:
    """Bottle detection using YOLO."""
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def bottle_detect(self, frame):
        results = self.model(frame)
        for box in results[0].boxes:
            if int(box.cls) == 39:  # Class ID 39 is for a bottle
                x, y, x2, y2 = map(int, box.xyxy[0])
                return frame, (x + x2) // 2, (y + y2) // 2
        return frame, None, None


def main():
    rclpy.init()
    node_classes = [Aruco, Orange, Bottle]
    nodes = [cls() for cls in node_classes]

    try:
        rclpy.spin(nodes[0])  # Run the first node (they all publish separately)
    except KeyboardInterrupt:
        pass
    finally:
        for node in nodes:
            node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
