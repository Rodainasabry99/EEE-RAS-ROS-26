from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    safety_zone = LaunchConfiguration('safety_zone')

    return LaunchDescription([

        DeclareLaunchArgument(
            'safety_zone',
            default_value='1.0'
        ),

    
        Node(
            package='task12',
            executable='fleet_emulator',
            name='robot_0',
            parameters=[{
                'robot_position': '0,0',
                'robot_priority': 1
            }]
        ),

    
        Node(
            package='task12',
            executable='fleet_emulator',
            name='robot_1',
            parameters=[{
                'robot_position': '0.5,0.5',
                'robot_priority': 5
            }]
        ),


        Node(
            package='task12',
            executable='fleet_emulator',
            name='robot_2',
            parameters=[{
                'robot_position': '1.1,1.1',
                'robot_priority': 2
            }]
        ),

        
        Node(
            package='task12',
            executable='traffic_manager',
            name='traffic_manager',
            parameters=[{
                'safety_zone': safety_zone
            }]
        ),

    ])