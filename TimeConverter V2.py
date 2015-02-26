'''Procedure'''
def procedured(hour, munute):
    '''time converter'''
    if hour >= 13:
        hour = hour-12
        if hour < 10:
            if munute < 10:
                print '0'+str(hour)+':0'+str(munute), 'PM'
            else:
                print '0'+str(hour)+':'+str(munute), 'PM'
        else:
            if munute < 10:
                print str(hour)+':0'+str(munute), 'PM'
            else:
                print str(hour)+':'+str(munute), 'PM'
    else:
        if hour < 10:
            if munute < 10:
                print '0'+str(hour)+':0'+str(munute), 'AM'
            else:
                print '0'+str(hour)+':'+str(munute), 'AM'
        else:
            if munute < 10:
                print str(hour)+':0'+str(munute), 'AM'
            else:
                print str(hour)+':'+str(munute), 'AM'
procedured(input(), input())
