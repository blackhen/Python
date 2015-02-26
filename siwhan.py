'''siwhan'''
def siwhan(word):
    '''siwhan'''
    siw = 'SIWHAN'
    ans = ''
    for i in word:
        if i not in siw:
            ans = ans+i
    return ans
print siwhan(raw_input())
