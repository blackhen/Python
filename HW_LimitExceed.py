'''
Challenge : HW_LimitExceed
Program : LimitExceed
Language : Phyton (Version 2.7.8)
Author : Jiravat Boonkumnerd
Date : 28/8/2557 00:19
'''
def limitexceed():
    '''
    Function name : limitexceed
    int(input) -> number > 1024 -> number(output)
    '''
    number_all = 0
    while number_all <= 1024:
        number_all += input()
    print number_all
limitexceed() 
