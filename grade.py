'''grade'''
def grade():
    '''grade'''
    grade1 = input()
    if grade1 > 80:
        print'A'
    elif grade1 >= 70 and grade1 < 80:
        print'B'
    elif grade1 >= 60 and grade1 < 70:
        print'C'
    elif grade1 >= 50 and grade1 < 60:
        print'D'
    elif grade1 < 50:
        print'F'
grade()
