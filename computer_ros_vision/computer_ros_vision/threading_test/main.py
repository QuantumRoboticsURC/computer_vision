import threading
import subprocess
import time

def run_ros2_publisher():
    subprocess.run(["python3", "zed_publisher.py"])

def run_websocket_server():
    subprocess.run(["python3", "zed_server.py"])

if __name__ == "__main__":
    ros2_thread = threading.Thread(target=run_ros2_publisher)
    ws_thread = threading.Thread(target=run_websocket_server)

    ros2_thread.start()
    time.sleep(2)  # Ensure ROS2 starts before WebSocket
    ws_thread.start()

    ros2_thread.join()
    ws_thread.join()
