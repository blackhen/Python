'''text'''
fff = open('file1_1.txt', 'r')
ggg = open('file1_2.txt', 'w')
print fff
for i in fff:
    ggg.write((i+i).replace('\n', '')+'\n')
fff.close()
ggg.close()

ggg = open('file1_2.txt', 'r')
lis = []
for i in ggg:
    lis.append(i)
ggg.close()

for i in range(len(lis)):
    if lis[i] != '':
        print lis[len(lis)-i-1]
