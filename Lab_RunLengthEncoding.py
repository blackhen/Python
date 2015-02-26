'''Lab_RunLengthEncoding'''
def encoding(text):
    '''return the lenght of repeat characters and the characters'''
    index = 0
    count = 0
    result = ''
    while index < len(text):
        if index == len(text)-1:
            count += 1
            result += str(count)+text[index]
            break
        elif text[index] != text[index+1]:
            count += 1
            result += str(count)+text[index]
            index += 1
            count = 0
        else:
            count += 1
            index += 1
    print result
encoding(raw_input())
