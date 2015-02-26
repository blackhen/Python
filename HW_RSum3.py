'''HW_RSum'''
def rsum(num):
    '''sum of all number to 1'''
    print sum(xrange(num, 1, abs(num)/-num))+1
rsum(input())
