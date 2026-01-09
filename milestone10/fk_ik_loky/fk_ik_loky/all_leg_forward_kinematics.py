import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import PointStamped

from fk_ik_loky.all_leg_fk_math import fk_all_leg

class FKAllNode(Node):
    def __init__(self):
        super().__init__('fk_all_legs')
        self.subscription = self.create_subscription(
            JointState, '/joint_states', self.joint_callback, 10
        )

        self.publisher = {}
        for legnum in range(1, 7):
            topic = f'/leg_{legnum}_end_effector'
            self.publisher[legnum] = self.create_publisher(
                PointStamped, topic, 10
            )

        self.get_logger().info('FK All Legs Node started!')
    
    def joint_callback(self, msg):
        log_msg = ""
        for i in range(1, 7):
            try:
                idx_coxa = msg.name.index(f'leg{i}_coxa_joint')
                idx_femur = msg.name.index(f'leg{i}_femur_joint')
                idx_tibia = msg.name.index(f'leg{i}_tibia_joint')

                t1 = msg.position[idx_coxa]
                t2 = msg.position[idx_femur]
                t3 = msg.position[idx_tibia]

                pos = fk_all_leg(i, t1, t2, t3)

                point_msg = PointStamped()
                point_msg.header.stamp = self.get_clock().now().to_msg()
                point_msg.header.frame_id = 'base_link'
                point_msg.point.x = float(pos[0])
                point_msg.point.y = float(pos[1])
                point_msg.point.z = float(pos[2])
                self.publisher[i].publish(point_msg)

                # self.get_logger().info(
                #     f'Leg {i} End effector: ({pos[0]:.5f}, {pos[1]:.5f}, {pos[2]:.5f})',
                #     throttle_duration_sec=2.0
                # )

                # simpan dulu msg nya
                log_msg += f"leg {i} : ({pos[0]:.5f}, {pos[1]:.5f}, {pos[2]:.5f})\n"

            except ValueError as e:
                self.get_logger().error(f'Error in joint names: {e}') 

        # print semua sekali, throttle biar nggak spam
        self.get_logger().info(f'\n{log_msg}', throttle_duration_sec=2.0)

def main(args=None):
    rclpy.init(args=args)
    node = FKAllNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

