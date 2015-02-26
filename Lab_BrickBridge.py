'''
Challenge : Lab_BrickBridge
Program : BrickBridge
Language : Phyton (Version 2.7.8)
Author : Natthawee Chutianusornchai
         Jiravat Boonkumnerd
Date : 21/8/2557 14:38
'''
def bridge_constructer(brick_small, brick_big, bridge_long):
    '''
    Function name : bridge construct calculator
    int((brick_small, brick_big, bridge_long)) -> str(small_brick)
    '''
    if brick_big * 5 > bridge_long: #Check big brick unuse
        while brick_big * 5 > bridge_long: 
            brick_big -= 1
        if brick_big * 5 + brick_small < bridge_long:
            print '-1'
        else:
            print bridge_long - brick_big * 5
    elif brick_big * 5 + brick_small < bridge_long:
        print '-1'
    else:
        print bridge_long - brick_big * 5
bridge_constructer(int(raw_input()), int(raw_input()), int(raw_input()))
