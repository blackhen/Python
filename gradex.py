'''Grade'''
def grade(med, mid):
    '''grade'''
    if med <= 100 and mid <= 100:
        med2 = med*30/100
        mid2 = mid*70/100
        grad = med2+mid2
        if grad >= 80:
            print 'A'
        elif grad >= 70:
            print 'B'
        elif grad >= 60:
            print 'C'
        elif grad >= 50:
            print 'D'
        elif grad < 50:
            print 'F'
grade(input(), input())
