# linear interpolation : (1-t)*P0 + t*P1
# kalau pake de casteljau algorithm 


# kalau pake bernstein polynomial:
def bezier_curve(t, p0, p1, p2, p3):
    k0 = (1-t)**3
    k1 = 3*t*(1-t)**2
    k2 = 3*t**2*(1-t)
    k3 = t**3

    x = k0*p0[0] + k1*p1[0] + k2*p2[0] + k3*p3[0]
    y = k0*p0[1] + k1*p1[1] + k2*p2[1] + k3*p3[1]
    z = k0*p0[2] + k1*p1[2] + k2*p2[2] + k3*p3[2]

    return [x, y, z]