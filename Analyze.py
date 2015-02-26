'''Analyze'''
def sentence(string):
    '''check'''
    dic = {}
    string = string.split()
    for i in string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        lis = sorted(dic.keys())
    for i in lis:
        print i+':'+str(dic[i])
sentence(raw_input())
