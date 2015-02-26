'''factorial'''
def factorial(n_1, num2):
    '''factorial'''
    out = 1
    num2 = len(num2)
    num = ((n_1-1)+num2)/num2
    for i in range(num):
        i = i+1
        out = out*n_1
        n_1 = n_1-num2
    print out
factorial(input(), raw_input())
