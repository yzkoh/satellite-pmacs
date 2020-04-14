from numpy import pi as PI

def rad2deg(x):
    return x * 180 / PI

def deg2rad(x):
    return x * PI / 180

def getCylinderVolume(diameter, length):
    return PI * (diameter/2) ** 2 * length