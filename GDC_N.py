'''
GCD_N
'''
def all(main()):
    '''
    find gdc
    '''
    lis = []
    for i in xrange(input()):
        lis.append(input())
        i = i
    for j in xrange(min(lis), 0, -1):
        for k in lis:
            if k % j == 0:
                return j
print main()
