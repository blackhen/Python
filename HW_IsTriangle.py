'''
Challenge : HW_IsTriangle
Program : IsTriangle
Language : Phyton (Version 2.7.8)
Author : Jiravat Boonkumnerd
Date : 21/8/2557 14:38
'''
def is_triangle(number_one, number_two, number_tree):
    '''
    Function name : right triangle check
    int(number_one, number_two, number_tree) -> str(Yes. or No.)
    '''
    if number_one**2 == number_two**2 + number_tree**2:
        print 'Yes.'
    elif number_two**2 == number_one**2 + number_tree**2:
        print 'Yes.'
    elif number_tree**2 == number_two**2 + number_one**2:
        print 'Yes.'
    else:
        print 'No.'
is_triangle(input(), input(), input())
