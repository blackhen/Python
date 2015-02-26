'''smiley'''
def smil(loop):
    if loop == -1:
        print ':'
    if loop == 0:
        print ':-'
    if loop >= 1:
        print ':-'+')'*loop
    if loop > 1:
        loop = loop+2
    else:
        loop = loop+1
    smil(loop)
smil(-1)
