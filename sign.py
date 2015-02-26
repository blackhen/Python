'''sign'''
def sign(word1, word2, word3):
    '''sign'''
    for i in xrange(max(len(word1), len(word2), len(word3))+1):
        sp1 = " "
        sp2 = " "
        sp3 = " "
        if i < len(word1):
            sp1 = word1[i]
        if i < len(word2):
            sp2 = word2[i]
        if i < len(word3):
            sp3 = word3[i]
        print sp1, sp2, sp3
sign(raw_input(), raw_input(), raw_input())

    if word[-1] == "(":
        print 'NO'
    if word[0] == ")":
        print 'NO'
