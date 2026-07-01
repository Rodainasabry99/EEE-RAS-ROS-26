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
        self.SAFE_DISTANCE = 1.0

        self.robots = ["robot_0", "robot_1", "robot_2"]

        for r in self.robots:
            self.create_subscription(
                Pose2D,
                f'/{r}/position',
                lambda msg, name=r: self.pose_callback(msg, name),
                10
            )

            self.create_subscription(
                Int32,
                f'/{r}/priority',
                lambda msg, name=r: self.priority_callback(msg, name),
                10
            )

        self.create_timer(0.2, self.check_traffic)

    def pose_callback(self, msg, name):
        self.positions[name] = (msg.x, msg.y)

    def priority_callback(self, msg, name):
        self.priorities[name] = msg.data

    def distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def check_traffic(self):

        robots = list(self.positions.keys())

        self.get_logger().info(f"ROBOTS: {robots}")

        for i in range(len(robots)):
            for j in range(i + 1, len(robots)):

                r1 = robots[i]
                r2 = robots[j]

                p1 = self.positions[r1]
                p2 = self.positions[r2]

                d = self.distance(p1, p2)

                pr1 = self.priorities.get(r1, 0)
                pr2 = self.priorities.get(r2, 0)

                if d < self.SAFE_DISTANCE:
                    if pr1 < pr2:
                        self.get_logger().warn(
                            f"DANGER: {r1} yields to {r2} | distance={d:.2f}"
                        )
                    elif pr2 < pr1:
                        self.get_logger().warn(
                            f"DANGER: {r2} yields to {r1} | distance={d:.2f}"
                        )
                    else:
                        self.get_logger().warn(
                            f"DANGER: equal priority {r1} & {r2} | distance={d:.2f}"
                        )
                else:
                    self.get_logger().info(
                        f"CLEAR: {r1} & {r2} safe | distance={d:.2f}"
                    )


def main(args=None):
    rclpy.init(args=args)
    node = TrafficManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
