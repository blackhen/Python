'''fibonacci'''
def think(num):
    '''think'''
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return think(num-1)+think(num-2)
print think(input())
