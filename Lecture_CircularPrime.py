'''lecture_circularprime'''
def circular_prime(numbers):
    '''find sum of circular prime numbers'''
    prime1 = []
    prime_cir = []
    for chk_p in range(2, numbers + 1):
        if isinstance(chk_prime(chk_p), int):
            prime1.append(chk_prime(chk_p))
    for circ in prime1:
        if len(str(circ)) == 1:
            prime_cir.append(circ)
        else:
            count = 0
            for change in range(1, len(str(circ))):
                num = (str(circ) * 2)[change:(len(str(circ))) + change]
                if isinstance(chk_prime(int(num)), str):
                    break
                else:
                    count += 1
            if count == len(str(circ)) - 1:
                prime_cir.append(circ)
    print sum(prime_cir)
def chk_prime(number):
    '''check prime numbers'''
    check = 0
    for numm in range(2, int(number ** 0.5) + 1):
        if number % numm == 0:
            check = 1
            return 'not prime'
    if check == 0:
        return number
circular_prime(input())
