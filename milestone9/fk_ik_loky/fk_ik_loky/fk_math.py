import numpy as np

# def rotation_z(theta):
#     c, s = np.cos(theta), np.sin(theta)
#     return np.array([[c, -s, 0, 0],
#                      [s, c, 0, 0],
#                      [0, 0, 1, 0],
#                      [0, 0, 0, 1]])

# def rotation_y(theta):
#     c, s = np.cos(theta), np.sin(theta)
#     return np.array([[c, 0, s, 0],
#                      [0, 1, 0, 0],
#                      [-s, 0, c, 0],
#                      [0, 0, 0, 1]])

def translation_xyz(x,y,z):
    return np.array([[1, 0, 0, x],
                     [0, 1, 0, y],
                     [0, 0, 1, z],
                     [0, 0, 0, 1]])

def homogeneous_transform_rotZ(theta, x, y, z):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, -s, 0, x],
                     [s, c, 0, y],
                     [0, 0, 1, z],
                     [0, 0, 0 , 1]])

def homogeneous_transform_rotY(theta, x, y, z):
    c, s = np.cos(theta), np.sin(theta)
    return np.array([[c, 0, s, x],
                     [0, 1, 0, y],
                     [-s, 0, c, z],
                     [0, 0, 0 , 1]])

def fk_math(theta1, theta2, theta3):
    # T0 = translation_xyz(0, -0.086603, 0.08694) @ rotation_z(-np.pi/2)
    # T1 = translation_xyz(0, 0, -0.06344) @ rotation_z(theta1)
    # T2 = translation_xyz(0.025, 0, 0) @ rotation_y(-theta2)
    # T3 = translation_xyz(0.055, 0, 0) @ rotation_y(theta3)
    # T4 = translation_xyz(0, 0, -0.071429)
    
    # Main amannya langsung pake homogeneous matrix ygy
    T0 = homogeneous_transform_rotZ(-np.pi/2, 0, -0.086603, 0.08694)
    T1 = homogeneous_transform_rotZ(theta1, 0, 0, -0.06344)
    T2 = homogeneous_transform_rotY(-theta2, 0.025, 0, 0)
    T3 = homogeneous_transform_rotY(theta3, 0.055, 0, 0)
    T4 = translation_xyz(0, 0, -0.071429)
    
    matrix = T0 @ T1 @ T2 @ T3 @ T4
    position = matrix[:3, 3]
    return position