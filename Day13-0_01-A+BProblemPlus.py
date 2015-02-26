'''Day13-0_01-A+BProblemPlus'''
def problemplus(loop):
    '''think'''
    for i in range(loop):
        word2 = map(int, raw_input().split())
        think = 0
        for i in range(2):
            think = think + word2[i]
        print think
problemplus(input())
