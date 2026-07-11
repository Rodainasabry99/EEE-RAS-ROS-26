import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable, TimerAction
from launch_ros.actions import Node


def generate_launch_description():

    package_name = 'task14_pkg'

    pkg_share = get_package_share_directory(package_name)

    # World file
    world_path = os.path.join(
        pkg_share,
        'worlds',
        'task14_world.sdf'
    )

    # TurtleBot3 models path
    turtlebot3_path = get_package_share_directory(
        'turtlebot3_gazebo'
    )

    models_path = os.path.join(
        turtlebot3_path,
        'models'
    )

    robot_model = os.path.join(
        models_path,
        'turtlebot3_burger',
        'model.sdf'
    )


    # Gazebo needs model path
    set_model_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=models_path
    )


    # Select TurtleBot3 burger
    set_turtlebot_model = SetEnvironmentVariable(
        name='TURTLEBOT3_MODEL',
        value='burger'
    )


    # Start Gazebo with custom world
    gazebo = ExecuteProcess(
        cmd=[
            'gz',
            'sim',
            world_path,
            '-r'
        ],
        output='screen'
    )


    # Spawn TurtleBot3
    spawn_robot = TimerAction(
        period=3.0,
        actions=[
            Node(
                package='ros_gz_sim',
                executable='create',
                arguments=[
                    '-name',
                    'turtlebot3_burger',
                    '-file',
                    robot_model,
                    '-x',
                    '0',
                    '-y',
                    '0',
                    '-z',
                    '0.2'
                ],
                output='screen'
            )
        ]
    )


    # Bridge ROS2 cmd_vel to Gazebo
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'
        ],
        output='screen'
    )


    # Autonomous movement node
    mover = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='task14_pkg',
                executable='autonomous_mover',
                output='screen'
            )
        ]
    )


    return LaunchDescription([
        set_model_path,
        set_turtlebot_model,
        gazebo,
        spawn_robot,
        bridge,
        mover
    ])