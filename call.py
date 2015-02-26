'''callsum'''
def check(num, step):
    '''callsum'''
    if num == 1 and step == 0:
        print 1
    elif num == 0:
        if step == -1:
            print 1
        else:
            print 'Error'
    elif step == 0:
        print 'Error'
    else:
        count = ((num-1)+step)/step
        if count == 1:
            print 1
        elif count <= 0:
            print 'Error'
        elif count % 1 == 0:
            print (count*(2+((count-1)*step)))/2
check(input(), input())
