'''
prime
'''
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
def main():
    '''main'''
    prim = 0
    for i in range(input()+1):
        if i == 2:
            prim += 1
        elif is_prime(i):
            prim += 1
        else:
            prim += 0
    print prim
main()
