import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor

from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

import random


class Robot(Node):

    def __init__(self, name, x, y, priority):
        super().__init__(name)

        self.name = name
        self.x = x
        self.y = y
        self.priority = priority

        self.pose_pub = self.create_publisher(
            Pose2D,
            f'/{name}/position',
            10
        )

        self.priority_pub = self.create_publisher(
            Int32,
            f'/{name}/priority',
            10
        )
        self.create_timer(0.1, self.publish_data)

    def publish_data(self):

        self.x += random.uniform(-0.03, 0.03)
        self.y += random.uniform(-0.03, 0.03)

        pose = Pose2D()
        pose.x = float(self.x)
        pose.y = float(self.y)
        pose.theta = 0.0

        pr = Int32()
        pr.data = int(self.priority)

        self.pose_pub.publish(pose)
        self.priority_pub.publish(pr)


def main(args=None):
    rclpy.init(args=args)

    robot_0 = Robot("robot_0", 0.0, 0.0, 1)
    robot_1 = Robot("robot_1", 0.5, 0.5, 5)
    robot_2 = Robot("robot_2", 1.1, 1.1, 2)

    executor = MultiThreadedExecutor()
    executor.add_node(robot_0)
    executor.add_node(robot_1)
    executor.add_node(robot_2)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass

    robot_0.destroy_node()
    robot_1.destroy_node()
    robot_2.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
