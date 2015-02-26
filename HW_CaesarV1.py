'''HW_CaesarV1'''
def caesar(digit, string):
    '''decode the string dat character is move by digit'''
    answer = ''
    list_cha_low = 'abcdefghijklmnopqrstuvwxyz'
    list_cha_upper = list_cha_low.upper()
    for i in string:
        if i in list_cha_low:
            answer = answer + list_cha_low[(list_cha_low.find(i)+digit)%26]
        elif i in list_cha_upper:
            answer = answer + list_cha_upper[(list_cha_upper.find(i)+digit)%26]
        else:
            answer = answer + i
    print answer
caesar(input(), raw_input())
