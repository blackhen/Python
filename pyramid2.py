'''pyramid'''
def pyramid(pyx):
    '''pyramid'''
    pyx2 = pyx
    pyx = (pyx*2)-1
    space = 0
    while space != pyx2:
        print (' '*space)+('*'*pyx)
        pyx = pyx-2
        space = space+1
pyramid(input())
