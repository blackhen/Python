'''pyramid'''
def pyramid(pyx):
    '''pyramid'''
    pyx = pyx - 1
    ggg = 1
    while pyx != -1:
        print (' '*pyx)+('*'*ggg)
        pyx = pyx-1
        ggg = ggg+2
pyramid(input())
