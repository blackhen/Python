'''checkparen'''
def check(word, ope, clo):
    '''check'''
    if word[-1] == "(":
        for i in word[0:-1]:
            if i == "(":
                ope = ope+1
            if i == ")":
                clo = clo+1
    elif word[0] == ")":
        for i in word[1:]:
            if i == "(":
                ope = ope+1
            if i == ")":
                clo = clo+1
    for i in word[0:]:
            if i == "(":
                ope = ope+1
            if i == ")":
                clo = clo+1
    if ope == clo:
        print 'YES'
    else:
        print 'NO'
check(raw_input(), 0, 0)
