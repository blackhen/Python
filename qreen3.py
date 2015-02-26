'''qreen3'''
def qreen(num2):
    '''qreen'''
    num = map(int, num2.split())
    inrow = num[0]
    incolum = num[1]
    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    for row in range(8):
        for  colum in range(8):
            if row == inrow or colum == incolum:
                board[row][colum] = 'x'
    board[inrow][incolum] = 'Q'
    print '-----------------'
    for row in range(8):
        space = abs(inrow-row)-1
        if space != -1:
            if space+1+incolum < 8:
                board[row][space+1+incolum] = 'x'
            if incolum-space-1 >= 0:
                board[row][incolum-space-1] = 'x'
        print '|'+'|'.join(board[row])+'|'
        print '-----------------'
qreen(raw_input())
