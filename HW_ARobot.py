'''
HW_ARobot
date: 25/8/2557 14:06
'''
def a_robot(number_robot):
    '''
    input number_robot  number_battery voltex volte_have
    output number battery want
    '''
    for i in range(number_robot):
        i = i
        number_battery = input()
        voltex = input()
        count_battery = 0
        for j in range(number_battery):
            j = j
            volte_have = input()
            if voltex > volte_have:
                count_battery += 1
        print count_battery
a_robot(input())
    
