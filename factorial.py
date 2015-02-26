'''Factorial'''
def factorial(number):
    '''factorial'''
    number2 = number - 1
    if number == 1:
        print 0
    elif number == 0:
        print 1
    else:
        while 1:
            number = number * number2
            number2 = number2 - 1
            if number2 == 0:
                break
        print number
factorial(input())
