from setuptools import find_packages, setup

package_name = 'computer_ros_vision'
submodules ="computer_ros_vision/submodules"

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name,submodules],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='quantum_main',
    maintainer_email='quantumrobotics.itesm@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['server=computer_ros_vision.zed_node:main'
        ],
    },
)
