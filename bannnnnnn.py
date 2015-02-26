'''BANNNNNN'''
def ban(word):
    '''bannn'''
    for i in range(input()):
        dee = raw_input().split('|')
        word.insert(int(dee[0]), dee[1])
    add = raw_input()
    while add in word:
        word.remove(add)
    for i in word:
        print i
ban(input())
