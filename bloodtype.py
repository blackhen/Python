'''bloodtype'''
def strin(num):
    '''bloodtype'''
    group = {'A':0, 'B':0, 'AB':0, 'O':0}
    for i in range(num):
        i = i
        string = raw_input()
        string = string.split(',')
        string = string[1]
        if string in group:
            group[string] = group.get(string, 0)+1
    print group['A']
    print group['B']
    print group['O']
    print group['AB']
strin(input())
