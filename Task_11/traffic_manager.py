mport rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32
import math


class TrafficManager(Node):
    def __init__(self):
        super().__init__('traffic_manager')
        self.positions = {}
        self.priorities = {}

        self.SAFE_DISTANCE = 1.0

        robots = ["robot_0", "robot_1", "robot_2"]

        for r in robots:
            self.create_subscription(Pose2D, f'/{r}/pose',
                                     lambda msg, name=r: self.pose_callback(msg, name), 10)

            self.create_subscription(Int32, f'/{r}/priority',
                                     lambda msg, name=r: self.priority_callback(msg, name),10)
        self.create_timer(0.5, self.check_traffic)

    def pose_callback(self, msg, name):
        self.positions[name] = (msg.x, msg.y)

    def priority_callback(self, msg, name):
        self.priorities[name] = msg.data

    def calculate_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def check_traffic(self):
        robots = list(self.positions.keys())
        for i in range(len(robots)):
            for j in range(i + 1, len(robots)):
                r1, r2 = robots[i], robots[j]
                if r1 not in self.positions or r2 not in self.positions:
                    continue

                p1 = self.positions[r1]
                p2 = self.positions[r2]

                d = self.calculate_distance(p1, p2)

                pr1 = self.priorities.get(r1, 0)
                pr2 = self.priorities.get(r2, 0)


                if d < self.SAFE_DISTANCE:

                    if pr1 < pr2:
                        self.get_logger().warn(
                            f"[DANGER] {r1} must yield to {r2} | dist={d:.2f}"
                        )
                    elif pr2 < pr1:
                        self.get_logger().warn(
                            f"[DANGER] {r2} must yield to {r1} | dist={d:.2f}"
                        )
                    else:
                        self.get_logger().info(
                            f"[CLEAR] Same priority | dist={d:.2f}"
                        )

                else:
                    self.get_logger().info("[CLEAR] Path is safe")


def main():
    rclpy.init()
    node = TrafficManager()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()


