import math

def clamp(value, min_val=-1.0, max_val=1.0):
    """Clamp value to valid acos range [-1, 1]"""
    return max(min_val, min(max_val, value))

def ik_adv(x, y, z):
    L0 = 0.9
    L1 = 0.7
    L2 = 0.5
    L3 = 0.3

    z_rel = z - L0
    x_rel = x
    y_rel = -y

    thetaC = math.atan2(y_rel, z_rel)
    z0 = math.sqrt(y_rel**2 + z_rel**2)
    thetaF1 = math.atan2(x_rel, z0-L1)
    a = math.sqrt(x_rel**2 + (z0-L1)**2)
    
    # Clamp to prevent math domain error when position is unreachable
    cos_thetaF2 = clamp((L2**2 + a**2 - L3**2) / (2 * a * L2))
    cos_thetaT = clamp((L2**2 + L3**2 - a**2) / (2 * L2 * L3))
    
    thetaF2 = math.acos(cos_thetaF2)
    thetaT_base = math.acos(cos_thetaT)

    thetaF = [thetaF1 + thetaF2, thetaF1 - thetaF2]
    thetaT = [thetaT_base - (math.pi), -thetaT_base + (math.pi)]

    return thetaC, thetaF, thetaT