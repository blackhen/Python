'''Hw_Seeker'''
def seeker(text):
    '''
    Input
    text to find summation of number

    Output
    summation of number in text
    '''
    ascii = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\
        abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in ascii:
        text = text.replace(i, ',')
    text = text.split(',')
    for i in range(text.count('')):
        text.pop(text.index(''))
    return sum(map(int, text))
print seeker(raw_input())
