for a in range(input()):
    n = input()
    l = []
    w = 0
    for b in range(n):
        str1 = raw_input().split()
        l.append(str1[1:len(str1)])
        w += len(str1[1:len(str1)])
    flag = 0
    l1 = raw_input().split()
    i = 0
    flag1 = 0
    for x in l1:
        for y in range(len(l)):
            if len(l[y]) != 0:
                l2 = l[y]
                if l2[-1] == x:
                    l2.pop(-1)
                    flag = 1
                    break
        if flag != 1:
            flag1 = 1
            break
        flag = 0
    if flag1 == 0 and w == len(l1):
        print 'Yes'
    else:
        print 'No'
'''
Input:
2
2
2 1 2
2 3 4
4 3 2 1
2
2 1 2
2 3 4
4 1 2 3

Output:
Yes
No'''