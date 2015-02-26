'''HW_HeadAndTail'''
def headandtail(number, list_number):
    '''headandtail(number of sum, list_number)
    sum of greater difference with sum of least
    '''
    minimum = 0
    maximum = 0
    list_number.sort()
    for i in range(number):
        minimum = minimum + list_number[i]
    for i in range(1, number+1):
        maximum = maximum + list_number[-i]
    print minimum+maximum 
headandtail(input(), input())
    
