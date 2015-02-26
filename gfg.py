''''pos_neg'''
def pos_neg():
    '''pos'''
    pos_x = input()
    pos_y = input()
    pos_a = raw_input()
    if pos_a == 'True':
        if pos_x < 0 and pos_y > 0 and pos_x != 0 and pos_y != 0:
            return True
        elif pos_x > 0 and pos_y < 0 and pos_x != 0 and pos_y != 0:
            return True
        else:
            return False
    else:
        if pos_x < 0 and pos_y < 0 and pos_x != 0 and pos_y != 0:
            return True
        elif pos_x > 0 and pos_y > 0 and pos_x != 0 and pos_y != 0:
            return True
        else:
            return False
def fff():
    '''fff'''
    if pos_neg():
        print 'True'
    else:
        print 'False'
fff()
