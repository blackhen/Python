'''patland'''
def pat(num):
    '''check'''
    num = int(num)
    while num >= 0:
        fff = ['a king.', 'a queen.', 'nobody.']
        for i in range(num):
            word = raw_input()
            bbb = 0
            while word[-1] == 'a':
                bbb = 1
                break
            while word[-1] == 'e':
                bbb = 1
                break
            while word[-1] == 'i':
                bbb = 1
                break
            while word[-1] == 'o':
                bbb = 1
                break
            while word[-1] == 'u':
                bbb = 1
                break
            while word[-1] == 'y':
                bbb = 2
                break
            print 'Case #'+str(i+1)+': '+word+' is ruled by '+fff[bbb]
        break
pat(input())
