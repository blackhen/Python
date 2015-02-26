'''Day14-1_04-SMS3310'''
def think(word):
    '''think'''
    code = {'a':'2', 'b':'22', 'c':'222',
            'd':'3', 'e':'33', 'f':'333',
            'g':'4', 'h':'44', 'i':'444',
            'j':'5', 'k':'55', 'l':'555',
            'm':'6', 'n':'66', 'o':'666',
            'p':'7', 'q':'77', 'r':'777',
            's':'7777', 't':'8', 'u':'88',
            'v':'888', 'w':'9', 'x':'99',
            'y':'999', 'z':'9999',
            ' ':'0', '':' '}
    ans = ''
    oldans = ''
    for i in word:
        if i != oldans and code[i][0] not in code[oldans]:
            ans += code[i]
        else:
            ans += ' '
            ans += code[i]
        oldans = i
    return ans
print think(raw_input())
