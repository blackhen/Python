'''primes'''
def prime(number, loop, check):
    '''primes'''
    if number >= 0:
        if loop > number:
            pass
        elif loop % 2 == 0 and loop != 2:
            prime(number, loop+1, check)
        elif loop % 3 == 0 and loop != 3:
            prime(number, loop+1, check)
        elif loop % 4 == 0 and loop != 4:
            prime(number, loop+1, check)
        elif loop % 5 == 0 and loop != 5:
            prime(number, loop+1, check)
        elif loop % 6 == 0 and loop != 6:
            prime(number, loop+1, check)
        elif loop % 7 == 0 and loop != 7:
            prime(number, loop+1, check)
        elif loop % 8 == 0 and loop != 8:
            prime(number, loop+1, check)
        elif loop % 9 == 0 and loop != 9:
            prime(number, loop+1, check)
        else:
            print loop, 'is a prime number.'
            prime(number, loop+1, check)
prime(input(), 2, 2)
