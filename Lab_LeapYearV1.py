'''
Challenge : Lab_LeapYearV1
Program : Check LeapYear
Language : Phyton (Version 2.7.8)
Author : Natthawee Chutianusornchai
         Jiravat Boonkumnerd
Date : 21/8/2557 15:22
'''
def check_leapyear(year_be):
    '''
    Function name : check_leapyear
    int(score) -> bool
    '''
    year_ad = year_be - 543
    if year_ad % 400 == 0:
        print True
    elif year_ad % 100 == 0:
        print False
    elif year_ad % 4 == 0:
        print True
    else:
        print False
check_leapyear(int(raw_input()))
