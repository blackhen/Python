"""Lab_AllSameDigit"""
def samedigit(num, num_check):
    """for check if A-input is all the same as B-input"""
    return 'yes' if num.find(num_check) == 0 else 'no'
print samedigit(raw_input(), raw_input())
