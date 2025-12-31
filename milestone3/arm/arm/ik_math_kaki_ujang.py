import math

def clamp(value, min_val=-1.0, max_val=1.0):
    """Clamp value to valid acos range [-1, 1]"""
    return max(min_val, min(max_val, value))

def ik_kaki_ujang(x, y, z):
    base = 0.45
    coxa = 0.25
    femur = 0.55
    tibia = 0.7149

    z_rel = z + base
    y_rel = -y
    x0 = math.sqrt(x**2 + y_rel**2)
    thetaF1 = math.atan2(z_rel, x0 - coxa)
    a = math.sqrt(z_rel**2 + (x0 - coxa)**2)
    cos_thetaF2 = clamp((femur**2 + a**2 - tibia**2)/(2 * a * femur))
    thetaF2 = math.acos(cos_thetaF2)
    cos_thetaT = clamp((femur**2 + tibia**2 - a**2)/(2 * femur * tibia))

    thetaC = math.atan2(y, x)
    thetaF = thetaF1 + thetaF2
    thetaT = math.acos(cos_thetaT) - (math.pi/2)

    return thetaC, thetaF, thetaT