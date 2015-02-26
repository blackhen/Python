'''Lab_Missing'''
def missing(number_digit):
    '''fide number missing'''
    list_number = []
    for i in range(number_digit):
        number_input = input()
        if number_input != 0:
            list_number.append(number_input)
        else:
            break
    for i in range(1, number_digit+1):
        if i not in list_number:
            print i
missing(input())
