'''math'''
def math():
    '''input(), input(), input()'''
    from math import cos, e, pi, sqrt, sin
    math_x = input()
    math_y = input()
    math_z = input()
    math_x = float(math_x)
    math_y = float(math_y)
    math_z = float(math_z)
    print (math_x**math_y) + math_z
    print cos(2*pi) + math_z
    print abs(math_x) + abs(math_y)
    print sqrt((math_x**2) + (math_y**2) + (math_z**2))
    print ((sin(math_x))**2) + ((cos(math_x))**2)
    print sqrt(math_x + math_y)
    print e*(math_x * math_y)
math()
