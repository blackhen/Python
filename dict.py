'''string'''
def string(string):
    '''string'''
    dic = dict()
    for i in string:
        dic[i] = dic.get(i,0)+1
        val = dic.values()
        val.sort(reverse=True)
    print dic
    for g in val:
        for h in dic.keys():
            if dic[h] == g:
                print h
                dic[h] = -1
string(raw_input())
