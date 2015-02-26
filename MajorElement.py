'''MajorElement'''
def stri(string):
    '''MajorElement'''
    string = string.split(',')
    dic = dict()
    for i in string:
        dic[i] = dic.get(i, 0)+1
        val = dic.values()
        val.sort(reverse=True)
    for i in dic.keys():
        if dic[i] == val[0]:
            if val[0] > (len(string))/2:
                print i
            else:
                print 'None'
                break
stri(raw_input())
