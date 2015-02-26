'''Lab_Olympic '''
def olympic(dic, count):
    '''sort score of the country'''
    for _ in range(input()):
        num = raw_input().split()
        num2 = num[1]+num[2]+num[3]
        if num2 not in dic:
            dic[num2] = dic.get(num2, [num[0]])
        else:
            dic[num2].append(num[0])
    sor = sorted(dic, reverse=1)
    for i in sor:
        ans = i[0]+' '+i[1]+' '+i[2]+' '+str(int(i[0])+int(i[1])+int(i[2]))
        dic[i].sort()
        print dic[i]
        for k in dic[i]:
            print str(count)+' '+k+' '+ans
        count += len(dic[i])
olympic({}, 1)
