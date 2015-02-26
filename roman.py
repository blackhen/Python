'''roman'''
def roman(word):
    '''test'''
    dic = {'M':1000,
           'D':500,
           'C':100,
           'L':50,
           'X':10,
           'V':5,
           'I':1,
           ' ':0}
    ans = 0
    for i in range(len(word)):
        if word[i] in dic.keys():
            if i != 0 and dic[word[i]] > dic[word[i-1]]:
                ans = ans + (dic[word[i]]-dic[word[i-1]]-dic[word[i-1]])
                print ans
            else:
                ans = ans + dic[word[i]]
                print ans
    print ans
roman(raw_input())
