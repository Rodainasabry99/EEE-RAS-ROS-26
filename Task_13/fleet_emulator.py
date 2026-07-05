import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import random


class Robot(Node):

    def __init__(self):
        super().__init__('robot')

        # Parameters coming from launch file
        self.declare_parameter('robot_position', '0,0')
        self.declare_parameter('robot_priority', 1)

        pos = self.get_parameter('robot_position').value
        self.priority = int(self.get_parameter('robot_priority').value)

        # convert position "x,y"
        x, y = pos.split(',')
        self.x = float(x)
        self.y = float(y)

        # Publishers (IMPORTANT FIX: unique topics per robot)
        self.pose_pub = self.create_publisher(
            Pose2D,
            f'/{self.get_name()}/position',
            10
        )

        self.priority_pub = self.create_publisher(
            Int32,
            f'/{self.get_name()}/priority',
            10
        )

        self.create_timer(0.1, self.publish_data)

    def publish_data(self):

        self.x += random.uniform(-0.03, 0.03)
        self.y += random.uniform(-0.03, 0.03)

        pose = Pose2D()
        pose.x = self.x
        pose.y = self.y
        pose.theta = 0.0

        pr = Int32()
        pr.data = self.priority

        self.pose_pub.publish(pose)
        self.priority_pub.publish(pr)


def main(args=None):
    rclpy.init(args=args)
    node = Robot()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()