'''HW_Safe'''
def key_lock(unlock, lock):
    '''number of spin key to lock'''
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = 0
    for i in range(len(unlock)):
        list_number = [string.find(unlock[i]), string.find(lock[i])]
        list_number.sort(reverse=True)
        if list_number[0] - list_number[1] <= 13:
            ans += list_number[0] - list_number[1]
        else:
            ans += (26-list_number[0])+list_number[1]
    return ans
print key_lock(raw_input(), raw_input())
