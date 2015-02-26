'''HW_ScaledMatrix'''
def scaledmatrit(number1, number2):
    '''find the scaled 0-1 of metrix and print in float 2 decimal'''
    list_matrix = []
    list_sort = []
    for i in range(number1*number2):
        input_number = input()
        list_matrix.append(input_number)
        list_sort.append(input_number)
    list_sort.sort()
    number_dif = list_sort[-1]-list_sort[0]
    for i in range(number1*number2):
        list_matrix[i] = (list_matrix[i]-list_sort[0])/number_dif
    for i in range(number1):
        ans = ''
        for k in range(number2):
            ans = ans+'%.2f' % (list_matrix[k+(number2*(i))])+' '
        print ans
scaledmatrit(input(), input())
        
            
            
        
