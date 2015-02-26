'''said'''
def said(num):
    '''fff'''
    ans = ''
    word = ['zero ', 'one ', 'two ', 'three ', 'four ', 'five ',
            'six ', 'seven ', 'eight ', 'nine ', 'ten ']
    for i in num:
        i = int(i)
        ans = ans + word[i]
    print ans
said(raw_input())
