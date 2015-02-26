"""HW_BinaryCompatator"""
def bin_num():
    """
    Check binary number for much value than other side will return 1
    """
    num = input()
    num2 = input()
    if num > num2:
        return '1 0' 
    elif num < num2:
        return '0 1'
    else:
        return '1 1'
print bin_num()
