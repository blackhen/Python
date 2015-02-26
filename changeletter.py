'''ChangeLetter'''
def chang(word, chan, number):
    '''change'''
    fff = len(word)
    if number > fff or number <= 0:
        print 'Error'
    else:
        print word[:number-1]+chan+word[number:]
chang(raw_input(), raw_input(), input())
