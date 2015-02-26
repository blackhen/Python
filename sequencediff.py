'''sequencesdif'''
def seq(string):
    '''num[1] - num[0] != num[i+1] - num[i]'''
    num = map(int, string.split())
    for i in xrange(len(num)):
        if num[1] - num[0] != num[i+1] - num[i]:
            return num[i+1]
print seq(raw_input())
