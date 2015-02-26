'''login'''
def login():
    '''login'''
    username = raw_input()
    password = raw_input()
    ffff = '*'*len(password)
    if username*3 == password:
        print 'User '+username+' Password '+ffff+'; Access granted!'
    else:
        print 'User '+username+' Password '+ffff+'; Access denied!'
login()
