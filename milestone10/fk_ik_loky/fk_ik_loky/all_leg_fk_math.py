import numpy as np

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

leg = {
    1: (0.075, 0.043301, 0.08694, 1/6*np.pi),
    2: (0.0, 0.086603, 0.08694, 3/6*np.pi),
    3: (-0.075, 0.043301, 0.08694, 5/6*np.pi),
    4: (-0.075, -0.043301, 0.08694, 7/6*np.pi),
    5: (0.0, -0.086603, 0.08694, 9/6*np.pi),
    6: (0.075, -0.043301, 0.08694, 11/6*np.pi),
}

def fk_all_leg(legnum, theta1, theta2, theta3):
    x_offset, y_offset, z_offset, base_angle = leg[legnum]

    T0 = homogeneous_transform_rotZ(base_angle, x_offset, y_offset, z_offset)
    T1 = homogeneous_transform_rotZ(theta1, 0, 0, -0.06344)
    T2 = homogeneous_transform_rotY(-theta2, 0.025, 0, 0)
    T3 = homogeneous_transform_rotY(theta3, 0.055, 0, 0)
    T4 = translation_xyz(0, 0, -0.071429)
    
    matrix = T0 @ T1 @ T2 @ T3 @ T4
    position = matrix[:3, 3]
    return position