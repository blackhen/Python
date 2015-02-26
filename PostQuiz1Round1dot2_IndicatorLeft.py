'''PostQuiz1Round1dot2_IndicatorLeft'''
def indicatorleft(width, height):
    '''print indicatorleft'''
    for i in range(height):
        print ' '*(height-i)+'*'*width
    print '*'*width
    for i in range(height):
        print ' '*(i+1)+'*'*width
indicatorleft(input(), input()/2)
