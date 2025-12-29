import numpy as np

def rotation_y(theta):
    c, s = np.cos(theta), np.sin(theta)
    # sb y nya tetap
    return np.array([[c, 0, s, 0],
                     [0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [0, 0, 0, 1]], dtype=float)

def translation_z(length):
    # ubah z sesuai length link
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, length],
                     [0, 0, 0, 1]], dtype=float)

def forward_kinematics_tabung_urdf(theta1, theta2):
   L0 = 9.0
   L1 = 7.0
   L2 = 5.0

   T0 = translation_z(L0)
   T1 = rotation_y(theta1) @ translation_z(L1)
   T2 = rotation_y(theta2) @ translation_z(L2)
   matrix = T0 @ T1 @ T2
   position = matrix[0:3, 3]
   return position


