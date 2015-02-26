'''number'''
def numberstair(number):
    '''numbrer'''
    number2 = 1
    number3 = 1
    floor = 2
    while number2 <= number:
        while number3 < floor:
            if number2 <= number:
                print number2,
            number2 = number2 + 1
            number3 = number3 + 1
        print ' '
        number3 = 1
        floor = floor + 1
numberstair(input())
