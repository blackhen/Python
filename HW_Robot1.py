'''
Challenge : HW_Robot1
Program : Check age
Language : Phyton (Version 2.7.8)
Author : Jiravat Boonkumnerd
Date : 25/8/2557 4:44
'''
def check_age(name, age):
    '''
    Function name : Check age
    input str(name), int(age) -> str
    '''
    if age < 18:
        print name+', you can pass.'
    else:
        print name+', you shall not pass.'
check_age(raw_input(), input())
