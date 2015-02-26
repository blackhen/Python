'''DayZ-SIWHAN'''
def think(string):
    '''DayZ-SIWHAN'''
    passage = 'SIWHAN'
    ans = ''
    for i in string:
        if i != passage[0] and i != passage[1] and i != passage[2]\
           and i != passage[3] and i != passage[4] and i != passage[5]:
            ans = ans+i
    print ans
think(raw_input())
