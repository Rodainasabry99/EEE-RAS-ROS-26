import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import math


class TrafficManager(Node):
    def __init__(self):
        super().__init__('traffic_manager')

        self.positions = {}
        self.priorities = {}

        self.robots = ['robot_0', 'robot_1', 'robot_2']

        for r in self.robots:
            self.create_subscription(Pose2D, f'/{r}/pose', self.pose_cb(r), 10)
            self.create_subscription(Int32, f'/{r}/priority', self.priority_cb(r), 10)

        self.timer = self.create_timer(0.2, self.check)

    def pose_cb(self, name):
        def cb(msg):
            self.positions[name] = (msg.x, msg.y)
        return cb

    def priority_cb(self, name):
        def cb(msg):
            self.priorities[name] = msg.data
        return cb

    def dist(self, a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    def check(self):
        my = 'robot_0'

        if my not in self.positions:
            return

        my_pos = self.positions[my]
        my_prio = self.priorities.get(my, 1)

        for r in self.robots:
            if r == my:
                continue

            if r in self.positions:
                d = self.dist(my_pos, self.positions[r])
                other = self.priorities.get(r, 1)

                if d < 1.0 and other > my_prio:
                    self.get_logger().warn(
                        f"[DANGER] Yield to {r} | dist={d:.2f}"
                    )
                    return

        self.get_logger().info("[CLEAR] Path safe")


def main():
    rclpy.init()
    node = TrafficManager()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()