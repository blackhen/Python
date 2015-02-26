'''bestword'''
def best(num):
    '''bestword'''
    dic = {'A':1, 'B':3, 'C':3, 'D':2, 'M':3, 'E':1, 'F':4, 'G':2, 'H':4,
           'I':1,
           'J':8, 'K':5, 'L':1, 'N':1, 'O':1, 'P':3, 'Q':10, 'R':1, 'S':1,
           'T':1,
           'U':1, 'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}
    if num >= 1 and num <= 20:
        for i in  range(num):
            dic2 = {}
            num1 = input()
            for i in range(num1):
                word = raw_input().upper()
                if len(word) <= 10:
                    number = 0
                    for i in word:
                        number = number + dic[i]
                    if number not in dic2:
                        dic2[number] = word
            ggg = sorted(dic2.keys(), reverse=True)[0]
            print dic2[ggg]
best(input())
