'''Dayz-|)uKe STYLE'''
def duck():
    '''change'''
    x20, y20 = map(int, raw_input().split())
    lis0 = []
    for i in range(y20):
        lis0.append(raw_input())
    x0, y0 = map(int, raw_input().split())
    word0 = raw_input()
    change(y20, x0, y0, word0, lis0)
    
def change(y2, x, y, word, lis):
    '''change'''
    lis[y][x] = word 
    for i in range(y2):
         print lis[i]
    
    
duck()
