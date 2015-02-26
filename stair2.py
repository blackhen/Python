'''numberstair2'''
def stair(num, num2, floor):
    '''numberstair'''
    space = (num-1)*2-1
    if num >= 0 and num <= 15:
        for iiii in range(num):
            iiii = iiii
            if space <= 0:
                space = 0
            elif space == 1:
                print ' '*space,
            else:
                print ' '*space,
            for fff in range(floor):
                fff = fff
                print str(num2),
                num2 = num2+1
            floor = floor +2
            print
            space = space-2
stair(input(), 1, 1)
