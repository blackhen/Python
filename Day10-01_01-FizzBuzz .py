'''fizzBuzz'''
def fizzbuzz(a_1, b_2, count):
    '''fizzbuzz'''
    start = 2
    if 1%a_1 == 0:
        answer = 'F'
    elif 1%b_2 == 0:
        answer = 'B'
    elif 1%a_1 == 0 and 1%b_2 == 0:
        answer = 'FB'
    else:
        answer = str(1)
    for num in range(count-1):
        num = num
        if start%a_1 == 0 and start%b_2 == 0:
            answer = answer+' FB'
        elif start%a_1 == 0:
            answer = answer+' F'
        elif start%b_2 == 0:
            answer = answer+' B'
        else:
            answer = answer+' '+str(start)
        start = start + 1
    print answer
fizzbuzz(input(), input(), input())
