'''qreen'''
def qreen(num2):
    '''qreen'''
    num = map(int,num2.split())
    g = 0
    board = []
    x = '| | | | | | | | |'
    for i in range(8):
        board.append(x)   
    #print board
    print '-----------------'

    for i in board:        
        if g == num[1]:
            print '|x|x|x|x|Q|x|x|x|'
        else:
            print i
            
                
        print '-----------------'
        g = g+1


    
qreen(raw_input())
