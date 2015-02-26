'''deeplen'''
def deeplen(zzz):
    '''if list[] >= 2:'''
    num = 0
    xxx = map(str, zzz)
    for i in xxx:
        if len(i) >= 2:
            num = num + len(i.split())
        else:
            num = num + 1
    print num
deeplen(input())
