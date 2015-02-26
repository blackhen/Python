'''Timeconverter'''
def time2(time):
    '''time check'''
    hour = time//3600
    time = time - hour*3600
    minute = time//60
    time = time - minute*60
    print str(hour)+' hours, '+str(minute)+' minutes, '+str(time)+' seconds.'
time2(input())
