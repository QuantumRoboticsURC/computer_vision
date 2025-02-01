import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/quantum_main/computer_vision/cv_ros/install/computer_ros_vision'
