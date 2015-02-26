'''linesorting'''
def linesrt(line):
    '''docstring'''
    from operator import itemgetter
    tup = []
    num = []
    for i in range(line):
        tup.append(raw_input())
        num.append(' ')
    for i in range(line):
        num[i] = len(tup[i])
    tab = zip(tup, num)
    tab.sort(key=itemgetter(1, 0))
    for i in range(line):
        print tab[i][0]
linesrt(input())
