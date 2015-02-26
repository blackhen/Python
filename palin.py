'''palindrome'''
def palin(num):
    '''palin'''
    out = ''
    for i in range(num):
        i = i
        word = raw_input()
        if word == word[::-1]:
            out = out+word+'\n'
    print out
palin(input())
