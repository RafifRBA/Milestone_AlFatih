import math

def inverse_kinematics_tabung_urdf(x, z, ccw):
    L0 = 9.0
    L1 = 7.0
    L2 = 5.0

    x_rel = x
    z_rel = z - L0

    r_squared = x_rel**2 + z_rel**2
    
    cos_theta2 = (r_squared - L1**2 - L2**2) / (2.0 * L1 * L2)
    cos_theta2 = max(-1.0, min(1.0, cos_theta2))
    
    if ccw:
        theta2 = math.acos(cos_theta2)
    else:
        theta2 = -math.acos(cos_theta2)

    k1 = L2 * math.sin(theta2)
    k2 = L1 + L2 * math.cos(theta2)

    theta1 = math.atan2(x_rel, z_rel) - math.atan2(k1, k2)
    
    return theta1, theta2