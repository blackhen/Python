'''Dayz-s0rT'''
def sord():
    '''sort'''
    dic = {}
    while True:
        word = map(float, raw_input().split())
        if word == [0.0, 0.0]:
            break
        for i in range(len(word)):
            if word[i]%1 == 0:
                word[i] = int(word[i])
        dic[word[1]] = dic.get(word[1], word[0])
    check = raw_input().lower()
    if check == 'min':
        lis = sorted(dic, reverse=True)
        for i in lis:
            if lis%1 == 0:
                print str('%.f')%lis, str(i)
            else:
                print str(dic[i]), str(i)
    if check == 'max':
        lis = sorted(dic)
        for i in lis:
            if lis%1 == 0:
                print str('%.f')%lis, str(i)  
            else:
                print str(dic[i]), str(i)
sord()
