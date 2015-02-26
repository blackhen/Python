'''ceasar'''
def cea(num, word):
    '''ceacar'''
    ans = ""
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = big.lower()
    for i in range(len(word)):
        if word[i].isupper():
            ans = ans+big[(big.find(word[i])+num)%len(big)]
        elif word[i].islower():
            ans = ans+small[(small.find(word[i])+num)%len(big)]
        else:
            ans = ans+word[i]
    print ans
cea(input(), raw_input())
