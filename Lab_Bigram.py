'''Lab_Bigram'''
def bigram(string):
    '''bigram'''
    dict_1 = {}
    for i in range(len(string)-2):
        word = string[i:i+2]#'iiiiii'
        number = 0
        for k in range(len(string)-1):
            if word == string[k:k+2]:
                number += 1
        dict_1[number] = dict_1.get(number, word)
    max_key = max(dict_1.keys())
    print dict_1[max_key]
    print max_key
bigram(raw_input())
