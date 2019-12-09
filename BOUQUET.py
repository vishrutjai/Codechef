for a in range(input()):
    test1 = map(int,raw_input().split())
    test2 = map(int,raw_input().split())
    test3 = map(int,raw_input().split())
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    if 0 not in test1:
        count = sum(test1)
    if 0 not in test2:
        count1 = sum(test2)
    if 0 not in test3:
        count2 = sum(test3)
    if 0 != test1[0] and 0 != test3[0] and 0 != test2[0]:
        count3 = test1[0] + test2[0] + test3[0]
    if 0 != test1[1] and 0 != test3[1] and 0 != test2[1]:
        count4 = test1[1] + test2[1] + test3[1]
    if 0 != test1[2] and 0 != test3[2] and 0 != test2[2]:
        count5 = test1[2] + test2[2] + test3[2]
    l = []
    l.append(count)
    l.append(count1)
    l.append(count2)
    l.append(count3)
    l.append(count4)
    l.append(count5)
    l.sort()
    c =  l[-1]
    if count ==0 and count1 ==0 and count2 ==0 and count3 ==0 and count4 ==0 and count5 ==0:
        print 0
    elif c % 2 == 0:
        print c - 1
    else:
        print c


'''
Input:
1
1 2 3
3 2 1
1 3 4

Output:
7'''