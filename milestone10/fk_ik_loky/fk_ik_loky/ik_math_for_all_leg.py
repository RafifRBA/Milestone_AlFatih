import math
import numpy as np

# IK untuk semua kaki loky

def clamp(value, min_val=-1.0, max_val=1.0):
    """Clamp value to valid acos range [-1, 1]"""
    return max(min_val, min(max_val, value))

def homogeneous_t0(x, y, z, theta):
    c, s = math.cos(theta), math.sin(theta)
    matrix = np.array([[math.cos(theta), -math.sin(theta), 0, x],
                     [math.sin(theta), math.cos(theta), 0, y],
                     [0, 0, 1, z],
                     [0, 0, 0, 1]])
    inv = np.linalg.inv(matrix)
    return inv

leg = {
    1: (0.075, 0.043301, 0.08694, 1/6*np.pi),
    2: (0.0, 0.086603, 0.08694, 3/6*np.pi),
    3: (-0.075, 0.043301, 0.08694, 5/6*np.pi),
    4: (-0.075, -0.043301, 0.08694, 7/6*np.pi),
    5: (0.0, -0.086603, 0.08694, 9/6*np.pi),
    6: (0.075, -0.043301, 0.08694, 11/6*np.pi),
}
def ik_all_kaki_loky(x, y, z, legnum):
    panjang_servocoxa_ke_servofemur = -0.06344
    coxa = 0.025
    femur = 0.055
    tibia = 0.071429

    x_leg, y_leg, z_leg, theta_leg = leg[legnum]

    inv_homogeneous_t0 = homogeneous_t0(x_leg, y_leg, z_leg, theta_leg)

    
    homogeneous_t1 = np.array(([math.cos(0), -math.sin(0), 0, 0],
                               [math.sin(0), math.cos(0), 0, 0],
                               [0, 0, 1, panjang_servocoxa_ke_servofemur],
                               [0, 0, 0, 1]))
    
    inv = np.linalg.inv(homogeneous_t1) @ inv_homogeneous_t0
    pos_rel = inv @ np.array([[x], [y], [z], [1]])

    x_rel = pos_rel[0, 0]
    y_rel = pos_rel[1, 0]
    z_rel = pos_rel[2, 0]


    # Bagian perhitungan IK
    x0 = math.sqrt(x_rel**2 + y_rel**2)
    thetaF1 = math.atan2(z_rel, x0 - coxa)
    a = math.sqrt(z_rel**2 + (x0 - coxa)**2)
    cos_thetaF2 = clamp((femur**2 + a**2 - tibia**2)/(2 * a * femur))
    thetaF2 = math.acos(cos_thetaF2)
    cos_thetaT = clamp((femur**2 + tibia**2 - a**2)/(2 * femur * tibia))

    thetaC = math.atan2(y_rel, x_rel)
    thetaF = (thetaF1 + thetaF2)
    thetaT = -(math.acos(cos_thetaT) - (math.pi/2))

    return thetaC, thetaF, thetaT