'''windmill'''
def wind():
    '''windmail'''
    number = input()
    bbbb = number
    space = number-1
    space2 = 1
    space3 = 0
    while 1:
        bbbb = number
        space = number-1
        space2 = 1
        space3 = 0
        while space != -1:
            print ('*'*space2)+(' '*space)+('*'*bbbb)+(' '*space2)+('*'*space2)+(' '*space)+('*'*bbbb)
            space2 = space2+1
            space = space-1
            bbbb = bbbb-1
            
        space = bbbb-1
        space2 = 1
        space3 = 0
        while space != -1:
            print (' '*space)+('*'*space2)+(' '*space3)+('*'*bbbb)+(' '*space)+('*'*space2)+(' '*space3)+('*'*bbbb)
            space = space-1
            space2 = space2+1
            space3 = space3+1
            bbbb = bbbb-1
            
        bbbb = number
        space = number-1
        space2 = 1
        space3 = 0
        while space != -1:
            print ('*'*space2)+(' '*space)+('*'*bbbb)+(' '*space2)+('*'*space2)+(' '*space)+('*'*bbbb)
            space2 = space2+1
            space = space-1
            bbbb = bbbb-1
            
        space = bbbb-1
        space2 = 1
        space3 = 0
        while space != -1:
            print (' '*space)+('*'*space2)+(' '*space3)+('*'*bbbb)+(' '*space)+('*'*space2)+(' '*space3)+('*'*bbbb)
            space = space-1
            space2 = space2+1
            space3 = space3+1
            bbbb = bbbb-1
wind()
