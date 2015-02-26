'''reverse'''
def reverse(num):
    '''reverse'''
    keeb = list()
    for i in range(num):
        i = i
        check = raw_input()
        check = check.split()
        keeb = keeb+check
    count = len(keeb)-1
    lenght = len(keeb)
    for i in range(lenght):
        i = i
        print '%.4f'%(int(keeb[count])**0.5)
        count = count-1
reverse(input())
