'''salary'''
def salary(num):
    '''salaly'''
    if num < 7000:
        per = 15
    if num < 15000 and num > 7000:
        per = 12
    if num < 25000 and num > 15000:
        per = 10
    if num < 50000 and num > 25000:
        per = 7
    if num > 50000:
        per = 4
    num = float(num)
    print num+(num*per/100)
    print num*per/100
    print str(per)+'%'
salary(input())
