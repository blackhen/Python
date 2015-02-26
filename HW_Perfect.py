'''HW_Perfect'''
def perf_check(number):
    '''check perfect number'''
    sum_num = 0
    for i in xrange(1, number):
        if number % i == 0:
            sum_num += i
    return sum_num == number

def sum_perf(num_loop):
    '''sum of perfect number in range'''
    sum_perf_number = 0
    for i in xrange(28, num_loop, 4):
        if perf_check(i) == True:
            sum_perf_number += i
    print sum_perf_number+6
sum_perf(input())
