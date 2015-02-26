'''HW_Amicable '''
def sumpropdiv(num1):
    '''returns sum of proper divisors of n'''
    dsum = 0
    for i in range(1, num1 / 2 + 1):
        if num1 % i == 0:
            dsum += i
    num2 = dsum
    return ami_check(num1, num2)

def ami_check(num1, num2):
    '''check amicable'''
    if num1 != num2:
        if num1 == sum(i for i in range(1, num2 // 2 + 1) if num2 % i==0):
            return num1 + num2
    return 0

def main():
    '''main loop funtun'''
    sum_all = 0
    maxnum = input()
    count = []
    for i in [220, 284, 1184, 1210, 2620, 2924, \
              5020, 5564, 6232, 6368, 10744, 10856, \
              12285, 14595, 17296, 18416, 63020, 66928, \
              66992, 67095, 69615, 71145, 76084, 79750, \
              87633, 88730, 100485, 122265, 122368]:
        incre = sumpropdiv(i)
        if i >= maxnum:
            break
        if incre != 0 and incre not in count:
            sum_all += incre
            count.append(incre)
    print sum_all
main()
