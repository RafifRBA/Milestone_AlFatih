import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

from arm.ik_math import inverse_kinematics_tabung_urdf

class EndEffectorListener(Node):
    def __init__(self):
        super().__init__('EE_listener')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(1.0, self.on_timer)

        # Buat ngecheck theta2 positif atau negatif
        self.subscribe = self.create_subscription(
             JointState, '/joint_states', self.check_joint_callback, 10
        )

        # Buat publish hasil IK
        self.publisher = self.create_publisher(
            JointState, '/calculate_theta', 10
        )

        self.get_logger().info('End Effector Listener Node started!')

    def check_joint_callback(self, msg):
         self.theta2 = msg.position[1] >= 0

    def on_timer(self):
        from_base = 'base_link'
        to_end_eff = 'end_effector'
        try:
            t = self.tf_buffer.lookup_transform(from_base, to_end_eff, rclpy.time.Time())

            # position
            p_x = t.transform.translation.x
            p_y = t.transform.translation.y
            p_z = t.transform.translation.z

            # quaternion
            # q_x = t.transform.rotation.x
            # q_y = t.transform.rotation.y
            # q_z = t.transform.rotation.z
            # q_w = t.transform.rotation.w
            sign = self.theta2
            theta1, theta2 = inverse_kinematics_tabung_urdf(p_x, p_z, sign)

            # publish hasil
            joint_msg = JointState()
            joint_msg.header.stamp = self.get_clock().now().to_msg()
            joint_msg.position = [theta1, theta2]
            self.publisher.publish(joint_msg)

            self.get_logger().info(
                f'\nEnd Effector:\n'
                f'Position: X = {p_x:.3f}, Y = {p_y:.3f}, Z = {p_z:.3f}'
                # f'Orientation: [{q_x:.3f}, {q_y:.3f}, {q_z:.3f}, {q_w:.3f}]'
                f'\nCalculated Thetas:\n'
                f'theta1 = {theta1:.3f}, theta2 = {theta2:.3f}'
            )

        except TransformException as ex:
            self.get_logger().info(f'Could not transform {from_base} to {to_end_eff}: {ex}')
            return
        
def main(args=None):
        rclpy.init(args=args)
        node = EndEffectorListener()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()