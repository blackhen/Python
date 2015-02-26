'''time'''
def time(loop, zzz):
    '''time'''
    if zzz == loop:
        print loop
    else:
        print zzz
        time(loop, zzz+1)
        print zzz
def time2(loop, zzz):
    '''time'''
    if zzz == loop:
        print loop
    else:
        print zzz
        time2(loop, zzz-1)
        print zzz
def cheak():
    '''check'''
    loop_2 = input()
    if loop_2 <= 50000 and loop_2 > 0:
        time(loop_2, 1)
    elif loop_2 >= -50000 and loop_2 < 0:
        time2(loop_2, 1)
    elif loop_2 == 0:
        print 1
        print 0
        print 1
cheak()
