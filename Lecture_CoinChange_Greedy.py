'''Lecture_CoinChange_Greedy'''
def coin_think(money):
    '''think coin form money input'''
    coin_1 = 0
    coin_5 = 0
    coin_10 = 0
    coin_25 = 0
    while 1:
        if money >= 25:
            coin_25 = money / 25
            money = money % 25
        elif money >= 10:
            coin_10 = money / 10
            money = money % 10
        elif money >= 5:
            coin_5 = money / 5
            money = money % 5
        elif money >= 1:
            coin_1 = money / 1
            money = money % 1
        else:
            return coin_1 + coin_5 + coin_10 + coin_25
print coin_think(input())
