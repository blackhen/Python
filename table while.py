'''multitable'''
def che(number2):
    '''check'''
    if 2 <= number2 and number2 <= 80:
        print 'n x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12'
        table(number2, 1, 2, 2)
def table(number, loop, floor, start):
    while True:     
        print start,
        start = start*2
        floor = floor+1
        if loop >= 12:
            print
            start = floor
        if floor <= number:
            break
che(input())
