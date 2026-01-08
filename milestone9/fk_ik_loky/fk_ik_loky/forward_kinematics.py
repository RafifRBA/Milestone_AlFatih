import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PointStamped

# Import dari file fk_math.py
from fk_ik_loky.fk_math import fk_math

class FKNode(Node):
    def __init__(self):
        super().__init__('forward_kinematics')
        
        self.subscription = self.create_subscription(
            JointState, '/joint_states', self.joint_callback, 10)
        
        self.publisher = self.create_publisher(
            PointStamped, '/end_effector_position', 10)
        
        self.get_logger().info('FK Node started!')

    def joint_callback(self, msg):
        theta1 = msg.position[0] if len(msg.position) > 0 else 0.0
        theta2 = msg.position[1] if len(msg.position) > 1 else 0.0
        theta3 = msg.position[2] if len(msg.position) > 2 else 0.0
        
        # Panggil fungsi dari fk_math
        pos = fk_math(theta1, theta2, theta3)
        
        # Publish hasil
        point_msg = PointStamped()
        point_msg.header.stamp = self.get_clock().now().to_msg()
        point_msg.header.frame_id = 'base_link'
        point_msg.point.x = float(pos[0])
        point_msg.point.y = float(pos[1])
        point_msg.point.z = float(pos[2])
        self.publisher.publish(point_msg)
        
        self.get_logger().info(f'End effector: ({pos[0]:.5f}, {pos[1]:.5f}, {pos[2]:.5f})')

def main(args=None):
    rclpy.init(args=args)
    node = FKNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()