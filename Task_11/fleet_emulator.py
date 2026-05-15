import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import sys


class Robot(Node):

    def __init__(self, name, x, y, p):
        super().__init__(name)

        self.name = name
        self.x = x
        self.y = y
        self.p = p

        self.pose_pub = self.create_publisher(Pose2D, f'/{name}/pose', 10)
        self.priority_pub = self.create_publisher(Int32, f'/{name}/priority', 10)

        self.create_timer(0.1, self.publish_data)

    def publish_data(self):

        pose = Pose2D()
        pose.x =float( self.x)
        pose.y =float (self.y)
        pose.theta = 0.0

        priority_msg = Int32()
        priority_msg.data =int(self.p)
            
        self.pose_pub.publish(pose)
        self.priority_pub.publish(priority_msg)
        self.get_logger().info(
            f'{self.name}: ({self.x:.2f}, {self.y:.2f}) Priority={self.p}'
        )

        self.x += 0.1
        self.y += 0.1


def main(args=None):
    rclpy.init(args=args)

    name = sys.argv[1]

    if name == "robot_0":
        node = Robot("robot_0", 0.0, 0.0, 1)
    elif name == "robot_1":
        node = Robot("robot_1", 0.05, 0.05, 5)
    else:
        node = Robot("robot_2", 5, 5, 2)

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()

