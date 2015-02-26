'''DayZ-DataStructure'''
def think(order):
    '''think'''
    data = map(int, raw_input().split())
    order = order.split()
    count = order[0]
    numorder = int(order[1])
    for i in range(numorder):
        chk = map(int, raw_input().split())
        if chk[0] == 1:
            start = chk[1]-1
            end = chk[2]
            for i in range(len(data[start:end])):
                data[start] = chk[3]
                start = start+1
        elif chk[0] == 2:
            start = chk[1]-1
            end = chk[2]
            step = chk[3]
            count = 1
            for i in range(len(data[start:end])):
                i = i
                if start+1 == end:
                    data[start] = data[start]+((chk[2]-chk[1]+1)*chk[3])
                else:
                    data[start] = data[start]+step
                    count = count+1
                    step = chk[3]*count
                    start = start+1
        elif chk[0] == 3:
            data.insert(chk[1]-1, chk[2])
        elif chk[0] == 4:
            start = chk[1]-1
            end = chk[2]
            ans = 0
            for i in range(len(data[start:end])):
                i = i
                ans = ans+data[start]
                start = start+1
            print ans
think(raw_input())
