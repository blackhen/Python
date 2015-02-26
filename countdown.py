'''countdown'''
def countdown(number):
    '''countdown'''
    if number <= 0:
        print 'BOOM!'
    else:
        countdown(number-1)
        print number
countdown(input())
