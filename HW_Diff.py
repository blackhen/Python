"""HW_Diff"""
def diff(num, num1):
    """
    this function use for check how defferent of
    couple number and single number in range
    """
    box = (sum(range(num, num1+1, 2)))-(sum(range(num+1, num1+1, 2)))
    if box <= 0:
        box = box*(-1)
    print box
diff(input(), input())
