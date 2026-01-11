import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

from fk_ik_loky.ik_math_for_all_leg import ik_all_kaki_loky

class InverseKinematics(Node):
    def __init__(self):
        super().__init__('inverse_kinematics_all_leg')
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(1.0, self.on_timer)

        self.publisher_ = {}
        for i in range(1, 7):
            topic = f'/theta_IK_leg{i}'
            self.publisher_[i] = self.create_publisher(
                JointState, topic, 10
            )

        self.get_logger().info('Inverse Kinematics for All Leg Node started!')

    def on_timer(self):
        from_base = 'base_link'

        for i in range(1, 7):
            to_end_effector = f'leg{i}_end_effector_link'

            try:
                t = self.tf_buffer.lookup_transform(from_base, to_end_effector, rclpy.time.Time())
           
                p_x = t.transform.translation.x
                p_y = t.transform.translation.y
                p_z = t.transform.translation.z

                coxa, femur, tibia = ik_all_kaki_loky(p_x, p_y, p_z, i)

                joint_msg = JointState()
                joint_msg.header.stamp = self.get_clock().now().to_msg()
                joint_msg.name = [f'leg{i}_coxa_joint', f'leg{i}_femur_joint', f'leg{i}_tibia_joint']
                joint_msg.position = [float(coxa), float(femur), float(tibia)]
                self.publisher_[i].publish(joint_msg)

                self.get_logger().info(
                    f'Leg {i} : \n'
                    f'X = {p_x:.3f}, Y = {p_y:.3f}, Z = {p_z:.3f} \n'
                    f'thetaC = {coxa:.3f}, thetaF = {femur:.3f}, thetaT = {tibia:.3f} \n'
                )

            except TransformException as ex:
                self.get_logger().info(f"Couldn't transform {from_base} to {to_end_effector}: {ex}")
                return
            


def main(args=None):
        rclpy.init(args=args)
        node = InverseKinematics()
        rclpy.spin(node)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()