'''HW_PED_PON_FIRE'''
def ped_pon_fire():
    '''
    Input
    Insert loop and energy of each ped

    Output
    Amoung of ped that can filght
    '''
    ped_oil = {}
    for i in xrange(input()):
        inpu = input()
        ped_oil[inpu] = ped_oil.get(inpu, 0)
        ped_oil[inpu] += 1
    success = input()
    count = 0
    for i in ped_oil:
        if success - i in ped_oil:
            count += ped_oil[i] * ped_oil[success - i]
    print count/2
ped_pon_fire()
