'''
Challenge : HW_Quadrant
Program : Quadrant
Language : Phyton (Version 2.7.8)
Author : Jiravat Boonkumnerd
Date : 30/8/2557 03:00
'''
def quadrant(point_x, point_y):
    '''
    Function name : Quadrant
    int(input)  -> Quadrant(output)
    '''
    if point_x < 0 and point_y > 0:
        print 'Q2'
    if point_x > 0 and point_y > 0:
        print 'Q1'
    if point_x < 0 and point_y < 0:
        print 'Q3'
    if point_x > 0 and point_y < 0:
        print 'Q4'
    if point_x == 0 and point_y != 0:
        print 'Y'
    if point_x != 0 and point_y == 0:
        print 'X'
    if point_x == 0 and point_y == 0:
        print 'O'
quadrant(input(), input())
