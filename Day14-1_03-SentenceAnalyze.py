'''Day14-1_03-SentenceAnalyze'''
def think(string):
    '''think'''
    diction = {}
    string = string.split()
    for i in string:
        if i in diction:
            diction[i] += 1
        else:
            diction[i] = 1
        list1 = sorted(diction.keys())
    for i in list1:
        print i + ':' + str(diction[i])
think(raw_input())
