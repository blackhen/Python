'''HW_RSum'''
def rsum(num):
    '''sum of all number to 1'''
    print sum(xrange(num, 1, -1 if num >= 1 else 1))+1
rsum(input())
