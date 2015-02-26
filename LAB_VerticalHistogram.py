'''lab_VerticalHistogram'''
def histogram(string):
    dic = {}
    space_2 = ''
    for i in string:
        dic[i] = dic[i] + 1 if i in dic else 1
    list_key = sorted(dic.keys())
    for i in range(max(dic.values()), 0, -1):
        space_1 = ''
        for j in list_key:
            space_1 += '  ' if dic[j] < i else ' *'
            if i <= 1:space_2 += j.swapcase() + ' ' 
        print '%.3d' % i + space_1
    print '    ' + space_2
histogram(raw_input().swapcase())
