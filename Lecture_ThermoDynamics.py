'''Lecture_ThermoDynamics'''
def heatdeath(list_number):
    '''heatdeath'''
    list_number.sort(reverse=True)
    number_ans = 0
    k = 1
    while k <= len(list_number):
        for i in range(len(list_number)-k):
            while list_number[i] - list_number[i+k] > 1:
                if list_number[i] - list_number[i+k] > 1:
                    list_number[i] -= 1
                    list_number[i+k] += 1
                    number_ans += 1
                if all(list_number[i] - list_number[i+1] <= 1 \
                       for i in range(len(list_number)-1)) == 0:
                    k = 1
        if all(list_number[i] - list_number[i+k] <= 1 \
               for i in range(len(list_number)-k)):
            k += 1
    print number_ans
heatdeath(input())
