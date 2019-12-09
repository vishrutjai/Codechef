test = raw_input().split()
l1 = []
l2 = []
for q in range(int(test[0])):
    l1.append(raw_input().split())
for w in range(int(test[1])):
    l2.append(raw_input().split())
for x in range(int(test[1])):
    c = l2[x]

    l4 = []
    for y in l1:
        if y[1] > l2[x][1]:
            continue
        elif y[0] < l2[x][0]:
            continue
        else:
            l4.append(y)
    l4.sort()
    if len(l4) == 1:
        print 1
    elif len(l4) == 0:
        print 0
    else:
        flag = 1
        for y in range(len(l4)-1):
            if l4[y][1] < l4[y+1][0]:
                flag += 1
        print flag









'''
Example

Input:
3 3
1 3
5 6
2 4
1 6
1 3
2 3

Output:
2
1
0
'''
















