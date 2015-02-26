'''PostQuiz1Round2dot2_ChristmasTree'''
def cristmas_tree(leaf, body):
    '''print the cristmastree'''
    for i in range(1, leaf+1):
        print ' '*(leaf-i)+'*'*i+'*'*(i-1)
    for i in range(body):
        print ' '*(leaf-2)+'---'
cristmas_tree(input(), input())
