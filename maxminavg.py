'''maxandminavg'''
def maxa(num):
    '''max'''
    num2 = map(int, num.split())
    print max(num2)
    print min(num2)
    print sum(num2)/float(len(num2))
maxa(raw_input())
