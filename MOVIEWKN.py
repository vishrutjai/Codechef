wow = input()
for h in range(wow):

    n = input()

    l1 = raw_input().split()

    l2 = raw_input().split()
    print l1
    print l2
    highest = 0
    r = int(l2[0])
    for i in range(n):
        if int(l1[i])*int(l2[i]) >= highest:
            highest = int(l1[i])*int(l2[i])
            if r > int(l2[i]):
                print 'hello'
                r = int(l2[i])
            else:
                continue
    print r
'''
Input:
2
2
1 2
2 1
4
2 1 4 1
2 4 1 4

Output:
1
2
'''