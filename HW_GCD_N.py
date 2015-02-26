'''
GCD_N
'''
def main(number_digit):
    '''
    find gdc
    '''
    lis = []
    for i in xrange(number_digit):
        lis.append(input())
        i = i
    for j in xrange(min(lis), 0, -1):
        count = 0
        for k in lis:
            if k % j == 0:
                count += 1
                if count >= len(lis):
                    return j
print main(input())
