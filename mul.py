def mal(x, y):
    if x<=1:
        return y
    else:
        ans = y + mal(x-1, y)
        return ans
answer = mal(4, 5)
print answer
