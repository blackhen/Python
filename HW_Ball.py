'''HW_Ball'''
def ball(height, count):
    '''calculate bounce ball'''
    if height >= 0.01:
        ball(height = height*3/5, count = count + 1)
    else:
        print count-1
ball(float(input()), 0)
