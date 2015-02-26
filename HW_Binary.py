'''HW_Binary'''
def binary(number, string=''):
    '''base 10 to binary not use [ ]
    for while range xrange bin oct hex int
    '''
    if number == 0 and string == '':
        print 0
    elif number <= 0:
        print string[::-1]
    else:
        string = string+str(number%2)
        number = number/2
        binary(number, string)
binary(input())
