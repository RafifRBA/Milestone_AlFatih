import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PointStamped

from arm.ik_math import inverse_kinematics_tabung_urdf

class IKNode(Node):
    def __init__(self):
        super().__init__('inverse_kinematics')

        self.checktheta2 = self.create_subscription(
            JointState, '/joint_states', self.joint_check_callback, 10
        )
        
        self.subscription = self.create_subscription(
            PointStamped, '/end_effector_position', self.end_callback, 10
        )

        self.publisher = self.create_publisher(
            JointState, '/calculate_theta', 10
        )

        self.get_logger().info('IK Node started!')

    def joint_check_callback(self, msg):
        self.theta2 = msg.position[1] >= 0

    def end_callback(self, msg):
        x = msg.point.x
        z = msg.point.z

        sign = self.theta2
        theta1, theta2 = inverse_kinematics_tabung_urdf(x, z, ccw=sign)

        joint_msg = JointState()
        joint_msg.header.stamp = self.get_clock().now().to_msg()
        joint_msg.position = [theta1, theta2]
        self.publisher.publish(joint_msg)

        self.get_logger().info(f'Sudut yang dibentuk dalam radians: theta1 = {theta1:.3f}, theta2 = {theta2:.3f} ')

def main(args=None):
    rclpy.init(args=args)
    node = IKNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
