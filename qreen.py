'''queenway'''
def queenway(qreen):
    num = map(int,qreen.split())
    for i in range(8):
        print '-----------------'
        if i == num[1]:
            print '|x|x|x|x|Q|x|x|x|'
        for i in range(7):
            if i == num[1]-4:
                print '|x'
            if i == num[1]:
                print '|x'
            else:
                print '| '
        
        print '|'
    print '-----------------'








queenway(raw_input())
