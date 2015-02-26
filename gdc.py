'''GDC'''
def gdc(num1, num2):
    while num1 % 6 == 0 and num2 % 6 == 0:
        num1 = num1/6
        num2 = num2/6
    while num1 % 5 == 0 and num2 % 5 == 0:
        num1 = num1/5
        num2 = num2/5
    while num1 % 4 == 0 and num2 % 4 == 0:
        num1 = num1/4
        num2 = num2/4
    while num1 % 3 == 0 and num2 % 3 == 0:
        num1 = num1/3
        num2 = num2/3
    while num1 % 2 == 0 and num2 % 2 == 0:
        num1 = num1/2
        num2 = num2/2
    print num1*num2
gdc(input(), input())
