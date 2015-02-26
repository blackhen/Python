'''linear'''
def line(string):
    '''ax + by + c = 0
    dx + ey + f = 0 '''
    num = map(float, string.split())
    aaa = num[0]
    bbb = num[1]
    ccc = num[2]
    ddd = num[3]
    eee = num[4]
    fff = num[5]
    xxx = ((eee*ccc)-(bbb*fff))/((bbb*ddd)-(aaa*eee))
    yyy = ((ccc*-1)-(aaa*xxx))/bbb
    print 'x = '+'%.3f' % xxx
    print 'y = '+'%.3f' % yyy
line(raw_input())
