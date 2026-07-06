from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    safety_zone = LaunchConfiguration('safety_zone')

    robot0_pos = LaunchConfiguration('robot0_position')
    robot0_pri = LaunchConfiguration('robot0_priority')

    robot1_pos = LaunchConfiguration('robot1_position')
    robot1_pri = LaunchConfiguration('robot1_priority')

    robot2_pos = LaunchConfiguration('robot2_position')
    robot2_pri = LaunchConfiguration('robot2_priority')

    return LaunchDescription([

        # arguments
        DeclareLaunchArgument('safety_zone', default_value='1.0'),

        DeclareLaunchArgument('robot0_position', default_value='0,0'),
        DeclareLaunchArgument('robot0_priority', default_value='1'),

        DeclareLaunchArgument('robot1_position', default_value='0.5,0.5'),
        DeclareLaunchArgument('robot1_priority', default_value='5'),

        DeclareLaunchArgument('robot2_position', default_value='1.1,1.1'),
        DeclareLaunchArgument('robot2_priority', default_value='2'),

        #el robots
        Node(
            package='task12',
            executable='fleet_emulator',
            name='robot_0',
            parameters=[{
                'robot_position': robot0_pos,
                'robot_priority': robot0_pri
            }]
        ),

        Node(
            package='task12',
            executable='fleet_emulator',
            name='robot_1',
            parameters=[{
                'robot_position': robot1_pos,
                'robot_priority': robot1_pri
            }]
        ),

        Node(
            package='task12',
            executable='fleet_emulator',
            name='robot_2',
            parameters=[{
                'robot_position': robot2_pos,
                'robot_priority': robot2_pri
            }]
        ),

        # 🔹 Traffic manager
        Node(
            package='task12',
            executable='traffic_manager',
            name='traffic_manager',
            parameters=[{
                'safety_zone': safety_zone
            }]
        ),

    ])