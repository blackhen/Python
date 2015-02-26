'''
HW_X
'''
def print_x(number):
    '''Function print x'''
    count = number+(number-3)
    for i in range(number-1):
        print '-'*i+'*'+'-'*(count)+'*'+'-'*i
        count -= 2
    print '-'*(number-1)+'*'+'-'*(number-1)
    count = 1
    for i in range(number-1):
        print '-'*(number-i-2)+'*'+'-'*(count)+'*'+'-'*(number-i-2)
        count += 2
print_x(input())
        
    
