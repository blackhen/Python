'''
HW_Almstmin
'''
def almstmin(number_loop):
    '''print Almost minimal of set number'''
    number_almstmin = 10000
    number_min = 10000
    if number_loop > 1 and number_loop <= 500:
        for i in range(number_loop):
            i = i
            number_in = input()
            if number_in < number_min:
                number_almstmin = number_min
                number_min = number_in
            elif number_in <= number_almstmin and number_in >= number_min:
                number_almstmin = number_in
        if number_min == number_almstmin:
            print 'NONE'
        else:
            print number_almstmin
    else:
        print 'NONE'
almstmin(input())
