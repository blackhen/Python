"""Lecture_Scout"""
def scout_egg(number):
    """for calculate if egg can put in pot"""
    for k in range(number):
        k = k
        list_egg = map(int, raw_input().split())
        list_w = map(int, raw_input().split())
        list_w.sort()
        weight = 0
        number_egg = 0
        for i in list_w:
            weight += i
            if weight > list_egg[2]:
                print number_egg
                break
            number_egg += 1
            if number_egg >= list_egg[1]:
                print list_egg[1]
                break
        if number_egg < list_egg[1] and weight <= list_egg[2]:
            print number_egg
scout_egg(input())
