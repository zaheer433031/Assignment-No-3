import math
def angle_MBC(AB, BC):
    theta_rad = math.atan2(AB, BC)
    theta_deg = round(theta_rad * (180 / math.pi))
    
    return theta_deg

AB = float(input())
BC = float(input())

angle = angle_MBC(AB, BC)
print("{}\u00b0".format(angle))