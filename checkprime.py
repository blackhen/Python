'''checkprime'''
def check(number):
    '''checkprint'''
    test = 1
    check2 = 0
    while test != number+1:
        if number % test == 0:
            check2 = check2 + 1
        test = test + 1
    if check2 == 2:
        print 'YES'
    else:
        print 'NO'
check(input())
