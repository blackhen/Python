'''
Challenge : Lab_OverlapCircle
Program : Circle overlapping checking
Language : Phyton (Version 2.7.8)
Author : Natthawee Chutianusornchai
         Jiravat Boonkumnerd
Date : 21/8/2557 14:38
'''
def is_overlapping():
    '''
    Function name : overlap check
    Input : point_x1(int), point_y1(int), round_1(int),
            point_x2(int), point_y2(int), round_2(int)
    Output : str
    '''
    point_x1 = input()
    point_y1 = input()
    round_1 = input()
    point_x2 = input()
    point_y2 = input()
    round_2 = input()
    from math import sqrt
    distance = sqrt((point_x2 - point_x1)**2 + (point_y2 - point_y1)**2)
    if round_1 + round_2 >= distance:
        print 'overlapping'
    else:
        print 'no overlapping'
is_overlapping()
