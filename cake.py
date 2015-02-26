'''cake'''
def caket():
    '''ceke'''
    cake = input()
    space = (cake*2)-3
    cake2 = 4
    print ' '*space+' ( ) '
    print ' '*space+'_|_|_'
    while space >= 2:
        space = space-1
        print ' '*space+'| '*cake2
        space = space-1
        print ' '*space+'_|'*cake2+'_'
        if space <= 0:
            break
        cake2 = cake2+2
    print '| '*cake2
    print '|_'*(cake2-1)+'|'
caket()
