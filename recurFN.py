'''recurFn'''
def recur(number):
    '''number'''
    if number > 100:
        return number - 10
    if number <= 100:
        return recur(recur(number+11))
print recur(input())
