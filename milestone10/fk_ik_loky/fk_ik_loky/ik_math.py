import math
import numpy as np

# IK untuk kaki pertama loky

def clamp(value, min_val=-1.0, max_val=1.0):
    """Clamp value to valid acos range [-1, 1]"""
    return max(min_val, min(max_val, value))

def ik_kaki_loky(x, y, z):
    panjang_servocoxa_ke_servofemur = -0.06344
    coxa = 0.025
    femur = 0.055
    tibia = 0.071429

    # Mengubah posisi x, y, z menjadi sama layaknya servo femur melihat end effector
    homogeneous_t0 = np.array([[math.cos(1/6 * math.pi), -math.sin(1/6 * math.pi), 0, 0.075],
                      [math.sin(1/6 * math.pi), math.cos(1/6 * math.pi), 0, 0.043301],
                      [0, 0, 1, 0.08694],
                      [0, 0, 0, 1]])
    
    homogeneous_t1 = np.array(([math.cos(0), -math.sin(0), 0, 0],
                               [math.sin(0), math.cos(0), 0, 0],
                               [0, 0, 1, panjang_servocoxa_ke_servofemur],
                               [0, 0, 0, 1]))
    
    inv = np.linalg.inv(homogeneous_t1) @ np.linalg.inv(homogeneous_t0)
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