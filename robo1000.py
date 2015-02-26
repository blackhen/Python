'''Robot1000'''
def robot(word):
    '''thinkl'''
    word = list(word)
    xxx = 0
    yyy = 0
    for i in word:
        if i == 'N':
            yyy = yyy+1
        elif i == 'E':
            xxx = xxx+1
        elif i == 'S':
            yyy = yyy-1
        elif i == 'W':
            xxx = xxx-1
        elif i == 'Z':
            yyy = 0
            xxx = 0
    print xxx, yyy
robot(raw_input())
