'''Multiply'''
def check(num, count, multi):
    '''multiplay'''
    multi = 0
    if num < 0 and count < 0:
        print multiply(abs(num), abs(count), 0)
    elif num == 0 or count == 0:
        print 0
    else:
        print multiply(num, count, 0)
def multiply(num, count, multi):
    '''multiplay'''
    if count <= 1:
        multi = multi + num
        return multi
    else:
        multi = multi + num
        return multiply(num, count-1, multi)
check(input(), input(), 0)
