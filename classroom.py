'''classroom'''
def classroom(aaa):
    '''classroom'''
    colum = aaa
    row = aaa
    lis = []
    for i in range(colum):
        lid = []
        for i in range(row):
            num = input()
            lid.append(num)
        lis.append(lid)
    for i in range(aaa):
        lis[i].sort()
    lis.sort(reverse=True)
    print lis[0][0]
classroom(input())
