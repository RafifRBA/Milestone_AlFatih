import rclpy
from rclpy.duration import Duration
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class TrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('trajectory_publisher')
        self.publisher = self.create_publisher(JointTrajectory, 'joint_trajectory_controller/joint_trajectory', 10)
        
        self.joint_names = ['joint_coxa', 'joint_femur', 'joint_tibia']
        self.get_logger().info("Trajectory Publisher Node has been started.")

    def publish_joints(self):

        msg = JointTrajectory()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.joint_names = self.joint_names

        point = JointTrajectoryPoint()
        point.positions = [0.5, 0.5, 0.5]
        point.time_from_start = Duration(seconds=2.0).to_msg()

        point2 = JointTrajectoryPoint()
        point2.positions = [-0.6, 1. , 0.8]
        point2.time_from_start = Duration(seconds=3.0).to_msg()

        point3 = JointTrajectoryPoint()
        point3.positions = [0 , 0 , 0]
        point3.time_from_start = Duration(seconds=5.0).to_msg()

        msg.points.append(point)
        msg.points.append(point2)
        msg.points.append(point3)
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = TrajectoryPublisher()
    node.publish_joints()
    rclpy.shutdown()

if __name__ == '__main__':
    main()