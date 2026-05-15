import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32


class Robot(Node):

    def __init__(self, name, x, y, p):
        super().__init__(name)

        self.name = name
        self.x = x
        self.y = y
        self.p = p

        self.pose_pub = self.create_publisher(
            Pose2D,
            f'/{name}/pose',
            10
        )

        self.priority_pub = self.create_publisher(
            Int32,
            f'/{name}/priority',
            10
        )

        self.timer = self.create_timer(0.1, self.publish_data)

    def publish_data(self):

        pose = Pose2D()
        pose.x = self.x
        pose.y = self.y
        pose.theta = 0.0

        priority_msg = Int32()
        priority_msg.data = self.p

        self.pose_pub.publish(pose)
        self.priority_pub.publish(priority_msg)

        self.get_logger().info(
            f'{self.name}: ({self.x:.2f}, {self.y:.2f}) Priority={self.p}'
        )

        self.x += 0.1
        self.y += 0.1


def main(args=None):

    rclpy.init(args=args)

    robot_0 = Robot("robot_0", 0.0, 0.0, 1)
    robot_1 = Robot("robot_1", 0.3,0.3, 5)
    robot_2 = Robot("robot_2", 5.0, 5.0, 2)

    executor = rclpy.executors.MultiThreadedExecutor()

    executor.add_node(robot_0)
    executor.add_node(robot_1)
    executor.add_node(robot_2)

    executor.spin()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
