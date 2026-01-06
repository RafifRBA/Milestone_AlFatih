import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import time

from leg_point_pub.bezier_curve import bezier_curve
from leg_point_pub.math_ik import ik_kaki_ujang
import numpy as np

class bezier_pub(Node):
    def __init__(self):
        super().__init__('bezier_publisher')
        self.publisher = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', 10)
        
        self.step_duration = 2.0
        self.joint_names = ['joint_coxa', 'joint_femur', 'joint_tibia']
        self.get_logger().info("Bezier Trajectory Publisher Node has been started.")
        
        # Tunggu sampai ada subscriber yang terhubung
        self.get_logger().info("Waiting for subscriber...")
        while self.publisher.get_subscription_count() == 0:
            time.sleep(0.1)
        self.get_logger().info("Subscriber connected!")

    def generate_step_trajectory(self):
        p0 = np.array([0.8, -0.8, -1.0])   
        p1 = np.array([0.8, -0.4, -0.6])  
        p2 = np.array([0.8, 0.4, -0.6])   
        p3 = np.array([0.8, 0.8, -1.0])

        t_values = np.linspace(0, 1, 20)
        traj_msg = JointTrajectory()
        traj_msg.header.stamp = self.get_clock().now().to_msg()
        traj_msg.joint_names = self.joint_names
        time_per_sample = self.step_duration / (len(t_values) - 1)

        for i, t in enumerate(t_values):
            xyz_point = bezier_curve(t, p0, p1, p2, p3)
            thetaC, thetaF, thetaT = ik_kaki_ujang(xyz_point[0], xyz_point[1], xyz_point[2])

            point = JointTrajectoryPoint()
            point.positions = [thetaC, thetaF, thetaT]

            time_sec = i * time_per_sample
            sec = int(time_sec)
            nanosec = int((time_sec - sec) * 1e9)
            point.time_from_start = Duration(seconds=sec, nanoseconds=nanosec).to_msg()

            traj_msg.points.append(point)

            print(f"t={t:.2f}, XYZ={xyz_point}")

        self.publisher.publish(traj_msg)
        self.get_logger().info(f"Published trajectory with {len(traj_msg.points)} points")

def main(args=None):
    rclpy.init(args=args)

    node = bezier_pub()
    node.generate_step_trajectory()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

