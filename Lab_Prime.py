def is_prime(num):
    '''
    precondition num is a nonnegative integer
    postcondition:  return True if num is prime and False otherwise.
    '''
    if num < 2:
        return False
    if num % 2 == 0:
        # return False
        return num == 2
    k = 3
    while k*k <= num:
        if num % k == 0:
            return False
        k += 2
    return True
def primecheck(number_main):
    number_ans = 0
    for i in range(number_main):
        
        if i%2 != 0:
            if i%3 !=0:
                if i%5 != 0:
                    if i%7 != 0:
                        number_ans += 1
    print number_ans
primecheck(input()) 
            
    
