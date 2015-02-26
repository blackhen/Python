'''gameshow'''
def game(word, num):
    '''gameshow'''
    word = list(word)
    for i in range(num):
        i = i
        word.append(word[0])
        word.pop(0)
    print ''.join(word)
game(raw_input(), input())
