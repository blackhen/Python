'''DIAmond'''
def diamond():
    '''diamons'''
    number = input()
    xxx = 1
    space = number - 1
    if number > 0:
        while space != -1:
            print ' '*space+'* '*xxx
            space = space - 1
            xxx = xxx + 1
        xxx = number - 1
        space = 1
        while xxx != 0:
            print ' '*space+'* '*xxx
            space = space + 1
            xxx = xxx - 1
diamond()
