def dgt(n):
    last = n%10
    new = n/10
    if n!= 0:
        return last + dgt(new)
    else:
        return last
print dgt(1324)
