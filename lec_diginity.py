"""Lecture_Diginity"""
def diginity(num):
    """for sum number in line"""
    return sum(map(int, num))

def digin():
    """this function made for diginity circuit"""
    box = []
    while True:
        num = raw_input()
        if int(num) == 0:
            break
        while int(num) >= 10:
            num = str(diginity(num))
        box.append(num)
    for i in box:
        print i
digin()
