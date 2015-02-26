'''Dayz-|)uKe STYLE!'''
def think():
    '''think'''
    house = []
    x_1, y_1 = map(int, raw_input().split())
    for i in range(y_1):
        house += [list(raw_input())]
    startx, starty = map(int, raw_input().split())
    chk = []
    def check(find, replace, posx, posy, chk):
        '''check'''
        if [posx, posy] not in chk:
            chk += [[posx, posy]]
        if [posx, posy+1] not in chk and posy+1 < x_1 \
           and house[posx][posy+1] == find:
            check(find, replace, posx, posy+1, chk)
        if [posx, posy-1] not in chk and posy-1 >= 0 \
           and house[posx][posy-1] == find:
            check(find, replace, posx, posy-1, chk)
        if [posx+1, posy] not in chk and posx+1 < y_1 \
           and house[posx+1][posy] == find:
            check(find, replace, posx+1, posy, chk)
        if [posx-1, posy] not in chk and posx-1 >= 0 \
           and house[posx-1][posy] == find:
            check(find, replace, posx-1, posy, chk)
        if house[posx][posy] == find:
            house[posx][posy] = replace
    check(house[starty][startx], raw_input(), starty, startx, chk)
    for i in house:
        print ''.join(i)
think()

