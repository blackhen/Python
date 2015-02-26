'''simplesorted'''
def simplesorted(string):
    '''check'''
    num = map(float, string.split())#num = list
    num.sort()
    for i in num:
        print '%.3f' % i,
simplesorted(raw_input())
