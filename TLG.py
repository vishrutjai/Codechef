a = input()
l = []
for x in range(a):
    i = []
    for y in range(1):
        n = raw_input().split()
        l.append(n)

highest = 0
winner = 0
for b in l:
    if int(b[0])>int(b[1]):
        if (int(b[0]) - int(b[1])) >highest:
            highest = (int(b[0]) - int(b[1]))
            winner = 1
    elif int(b[0]) == int(b[1]):
        continue
    else:
        if (int(b[1]) - int(b[0])) >highest:
            highest = (int(b[1]) - int(b[0]))
            winner = 2
l1 = []
l1.append(winner)
l1.append(highest)
for j in l1:
    print j,

'''
Input:
5
140 82
89 134
90 110
112 106
88 90
Output:
1 58
'''