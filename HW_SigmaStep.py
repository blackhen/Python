'''
HW_Sigmajump_num
'''
def signajump_num(start_point, end_point, jump_num):
    '''suum of number start_point to end'''
    if start_point == end_point:
        print start_point
    elif (start_point >= 0 and end_point >= 0 and jump_num > 0 \
          and start_point < end_point):# + < + + 
        print sum([x for x in xrange(start_point, end_point+1, jump_num)])
    elif (start_point >= 0 and end_point >= 0 and jump_num < 0 \
          and start_point > end_point):# + < + - 
        print sum([x for x in xrange(start_point, end_point+1, jump_num)])
    elif (start_point < 0 and end_point < 0 and jump_num < 0 \
          and start_point > end_point): #- > - -
        print sum([x for x in xrange(start_point, end_point-1, jump_num)])
    elif (start_point < 0 and end_point < 0 and jump_num > 0 \
          and start_point < end_point): #- < - +
        print sum([x for x in xrange(start_point, end_point-1, jump_num)])
    elif start_point < 0 and end_point >= 0 and jump_num > 0: #- + +
        print sum([x for x in xrange(start_point, end_point+1, jump_num)])
    elif start_point >= 0 and end_point < 0 and jump_num < 0: #+ - -
        print sum([x for x in xrange(start_point, end_point-1, jump_num)])
    else:
        print 'error'
signajump_num(input(), input(), input())
         
