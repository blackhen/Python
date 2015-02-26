'''Lecture_HorizontalHistogram'''
def histogram(string):
    '''histogram string'''
    dict_1 = {}
    for i in string.swapcase(): 
        dict_1[i] = dict_1.get(i, 0) + 1
    for i in dict_1:
        if dict_1[i] % 5 == 0:
            dict_1[i] = '-----|'*(dict_1[i]/5-1)+'-----'
        else:
            dict_1[i] = '-----|'*(dict_1[i]/5)+'-'*(dict_1[i]%5)
    list_1 = sorted(dict_1)
    for i in list_1:
        print i.swapcase()+' : '+dict_1[i]
histogram(raw_input())
