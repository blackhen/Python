'''palindrome'''
def palin(word):
    '''palin'''
    ggg = ''
    for i in range(word):
        i = i
        word2 = raw_input()
        if word2 == word2[::-1]:
            ggg = ggg+word2+'\n'
    print ggg
palin(input())
