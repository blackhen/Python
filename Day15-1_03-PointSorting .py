'''pointsort'''
def point(num):
    '''fefefef'''
    pigud = list()
    for i in range(num):
        point1 = input()
        point2 = input()
        point3 = '('+str(point1)+', '+str(point2)+')'
        rad = ((point1**2)+(point2**2))**0.5
        pigud.append((rad, point3))
    pigud.sort()
    for i in range(num):
        print pigud[i][1]
point(input())
