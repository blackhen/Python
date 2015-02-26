'''gene'''
def gene():
    '''gene'''
    word1 = raw_input()
    word2 = raw_input()
    for i in range(len(word2)):
        word = word2[i:]+word2[:i]
        print 'Type '+str(i+1)+' : '+word
        word1 = word1.replace(word, ('$'*len(word)))
    print 'Result : '+word1
gene()
