'''char'''
def hhhh(word):
    '''ghhh'''
    count = 0
    for i in word:
        if i.islower():
            count = count + 1
    print count
    count = 0
    for i in word:
        if i.isupper():
            count = count + 1
    print count
    print word.lower()
    print word.upper()
hhhh(raw_input())
