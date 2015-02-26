'''DayZ-Salary '''
def think(money):
    '''think'''
    add = 0
    if money < 7000:
        add = 0.15*money
        chk = '15%'
    elif 7000.01 <= money and money <= 15000.00:
        add = 0.12*money
        chk = '12%'
    elif 15000.01 <= money and money <= 25000.00:
        add = 0.10*money
        chk = '10%'
    elif 25000.01 <= money and money <= 50000.00:
        add = 0.07*money
        chk = '7%'
    elif 50000.01 <= money:
        add = 0.04*money
        chk = '4%'
    print float(money+add)
    print float(add)
    print chk
think(input())
