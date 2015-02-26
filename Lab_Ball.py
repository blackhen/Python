"""Lab_Ball"""
def magicball():
    """this program made for reproduce ball that hide in glass"""
    [left_ball, middle, rightball] = ['y', 'x', 'x']
    box = ''
    boxes = ''
    word = map(str, raw_input())
    for num in word:
        if num == 'A':
            box = left_ball
            boxes = middle
            left_ball = boxes
            middle = box
        elif num == 'B':
            box = middle
            boxes = rightball
            middle = boxes
            rightball = box
        elif num == 'C':
            box = left_ball
            boxes = rightball
            left_ball = boxes
            rightball = box
    if left_ball == 'y':
        print 1
    elif middle == 'y':
        print 2
    elif rightball == 'y':
        print 3
magicball()
