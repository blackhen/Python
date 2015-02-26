'''stair1'''
def stair(number):
    '''stair'''
    number2 = 1
    while number2 != number+1:
        print number2*'*'
        number2 = number2 + 1
stair(input())
