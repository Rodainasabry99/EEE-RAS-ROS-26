import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class AutonomousMover(Node):

    def __init__(self):
        super().__init__('autonomous_mover')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.move_robot
        )

        self.state = 0
        self.state_start = self.get_clock().now()

        self.get_logger().info("Autonomous Mover Started")


    def next_state(self):
        self.state += 1
        self.state_start = self.get_clock().now()


    def move_robot(self):

        msg = Twist()

        elapsed = (
            self.get_clock().now() - self.state_start
        ).nanoseconds / 1e9


        # 1- Move Forward
        if self.state == 0:
            msg.linear.x = 0.20

            if elapsed > 5.0:
                self.next_state()


        # 2- Turn Left
        elif self.state == 1:
            msg.angular.z = 0.60

            if elapsed > 2.60:
                self.next_state()


        # 3- Move Forward
        elif self.state == 2:
            msg.linear.x = 0.20

            if elapsed > 15.5:
                self.next_state()


        # 4- Turn Right
        elif self.state == 3:
            msg.angular.z = -0.60

            if elapsed > 2.60:
                self.next_state()


        # 5- Move Forward
        elif self.state == 4:
            msg.linear.x = 0.20

            if elapsed > 34:
                self.next_state()


        # 6- Turn right
        elif self.state == 5:
            msg.angular.z = -0.60

            if elapsed > 2.60:
                self.next_state()


        # 7- Move Forward
        elif self.state == 6:
            msg.linear.x = 0.20

            if elapsed > 35:
                self.next_state()


        # 8- Turn right
        elif self.state == 7:
            msg.linear.x = 0.0
            msg.angular.z =-0.60

            if elapsed > 2.60:
                self.next_state()


        # 9- Move Forward
        elif self.state == 8:
            msg.linear.x = 0.20
            msg.angular.z = 0.0

            if elapsed > 19.0:
                self.next_state()


        # 10- Turn right
        elif self.state == 9:
            msg.linear.x = 0.0
            msg.angular.z = -0.60

            if elapsed > 2.60:
                self.next_state()


        # 11- Move Forward
        elif self.state == 10:
            msg.linear.x = 0.20
            msg.angular.z = 0.0

            if elapsed > 20:
                self.next_state()

        # Stop
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = AutonomousMover()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()