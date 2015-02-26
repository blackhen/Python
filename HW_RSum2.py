'''HW_RSum'''
def rsum(num):
    '''sum of all number to 1'''
    print sum(i for i in xrange(num, 1, abs(num) - abs(num + 1)))+1
rsum(input())
