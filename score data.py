'''last score data'''
def last(numloop):
    '''last score data'''
    ans = []
    for i in range(numloop):
        word = raw_input().split()
        think = []
        think.append(word[2])
        think.append(-(int(word[0][3:])))
        think.append(word[1])
        ans.append(think)
    for i in range(numloop):
        ans[i][0] = float(ans[i][0])
    ans.sort(reverse=True)
    for i in range(numloop):
        print str(i+1)+'\t'+str('%.2f'%ans[i][0])+'\t'+\
              'pre'+str(-(ans[i][1]))+'\t'+ans[i][2]
last(input())
