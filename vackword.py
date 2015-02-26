'''backward'''
def backward(word):
    '''print'''
    if word == 'NULL':
        return word
    else:
        backward(raw_input())
        print word
backward(raw_input())
