'''
Challenge : Lab_Zero
Program : Zero
Language : Phyton (Version 2.7.8)
Author : Jiravat Boonkumnerd
        Karn Niamchan
Date : 1/9/2557 12:50
'''
def zer0():
    '''
    Function name : zer0
    input integer>0  -> integer
    '''
    number_sum = 0
    while 1:
        number_add = input()
        if number_add == 0:
            break
        number_sum += number_add
    print number_sum
zer0()
