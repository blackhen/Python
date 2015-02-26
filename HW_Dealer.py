'''HW_Dealer'''
def dealer(number_order):
    '''total price of order'''
    for _ in range(number_order):
        weight_spe = input()
        weight_nor = input()
        for _ in range(input()):
            weight = input()
            piece = input()
            if weight >= weight_spe:
                ans = piece+(piece*0.10)
            elif weight >= weight_nor:
                ans = piece+(piece*0.20)
            else:
                ans = piece
            print int(ans) if ans % 1 ==0 else int(ans) + 1
dealer(input())
