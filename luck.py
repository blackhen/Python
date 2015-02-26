'''Hello'''
def lucky_sum():
    '''lucky'''
    num1 = input()
    num2 = input()
    num3 = input()
    if num1 == 13:
        print 0
    elif num2 == 13:
        print num1
    elif num3 == 13:
        print num1+num2
    else:
        print num1+num2+num3
lucky_sum()
