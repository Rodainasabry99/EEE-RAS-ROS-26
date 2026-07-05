from setuptools import setup
from glob import glob
import os


package_name = 'task12'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    (os.path.join('share', package_name, 'launch'),
     glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rodaina-sabry',
    maintainer_email='rodaina-sabry@todo.todo',
    description='ROS2 Task12',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'fleet_emulator = task12.fleet_emulator:main',
            'traffic_manager = task12.traffic_manager:main',
        ],
    },
)
