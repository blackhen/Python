'''
Challenge : Lab_Grade
Program : Check grade
Language : Phyton (Version 2.7.8)
Author : Natthawee Chutianusornchai
         Jiravat Boonkumnerd
Date : 21/8/2557 14:10
'''
def grader(score):
    '''
    Function name : ckeck grade
    int(score) -> str(grade)
    '''
    if score <= 120 and score >= 100:
        print 'A'
    elif score <= 99 and score >= 95:
        print 'B+'
    elif score <= 94 and score >= 90:
        print 'B'
    elif score <= 89 and score >= 85:
        print 'C+'
    elif score <= 84 and score >= 80:
        print 'C'
    elif score <= 79 and score >= 75:
        print 'D+'
    elif score <= 74 and score >= 70:
        print 'D'
    elif score <= 69 and score >= 0:
        print 'F'
grader(int(raw_input()))
