"""Lecture_Key"""
def key(number):
    """for find code from summary + 3 of last number"""
    box = sum(map(int, number))+int(number[-3:])*10
    if box <= 999:
        box = box+1000
    elif box > 9999:
        box = str(box)[-4:]
    return box
print key(raw_input())
