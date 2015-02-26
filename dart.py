'''dart'''
def dart(loop):
    '''check'''
    if 1 <= loop and loop <= 100:
        score = 0
        for i in range(loop):
            i = i
            num = raw_input()
            num = map(int, num.split())
            xxx = num[0]
            yyy = num[1]
            zzz = ((xxx**2)+(yyy**2))**0.5
            if zzz <= 2:
                score = score+5
            elif zzz <= 4:
                score = score+4
            elif zzz <= 6:
                score = score+3
            elif zzz <= 8:
                score = score+2
            elif zzz <= 10:
                score = score+1
            else:
                score = score+0
    print score
dart(input())
