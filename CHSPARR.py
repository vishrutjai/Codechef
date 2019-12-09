a = input()
for hi in range(a):
    test1 = raw_input().split()
    test2 = raw_input().split()
    l = []
    l1 = []
    for y in range(int(test1[2])):
        if y == 1:
            count = 0
            for z in range(0,int(len(test2))-1):
                n = int(test2[count]) + int(test2[count+1])
                l1.append(int(test2[count]))
                l1.append(int(test2[count]) + int(test2[count+1]))
                #l.append(int(test2[count+1]))
                count += 1
        else:
            l2 = l[:]
            count = 0
            for z in range(0,int(len(l2))-1):
                n = int(l2[count]) + int(l2[count+1])
                l.append(int(l2[count]))
                l.append(int(l2[count]) + int(l2[count+1]))
                #l.append(int(test2[count+1]))
                count += 1

    print l

'''
Input:
2
3 1 1 5
1 6 9
3 2 6 7
1 6 9

Output:
38
36
'''