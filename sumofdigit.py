'''sumofdigit'''
def sumofdigit(number):
    '''number'''
    length = len(str(number))
    every = 0
    def think(num, length2, every2):
        '''think'''
        if length2 > 0:
            ans = num/(10**(length2-1))
            every2 = every2+ans
            think(num-(ans*(10**(length2-1))), length2-1, every2)
        else:
            print every2
    think(number, length, every)
sumofdigit(input())
