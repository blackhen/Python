'''
Challenge : HW_DotE
Program : DotE
Language : Phyton (Version 2.7.8)
Author : Jiravat Boonkumnerd
Date : 30/8/2557 03:37
'''
from math import factorial
def dote(number_player):
    '''
    Function name : DotE
    input int(player)  -> method(output)
    '''
    if number_player >= 1 and number_player <= 10:
        if number_player % 2 == 0:
            print (factorial(number_player))/(factorial(int(number_player-number_player/2))*(factorial(int(number_player/2))))
        else:
            print 2*((factorial(number_player))/(factorial(int(number_player-number_player/2))*(factorial(int(number_player/2)))))
dote(input())
