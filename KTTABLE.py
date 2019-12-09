a = input()
for hi in range(a):
    n = input()
    test = raw_input().split()
    test1 = raw_input().split()
    count = 0
    if len(test) == len(test1):
        if int(test[0]) >= int(test1[0]):
            count += 1
        for x in range(1,len(test)):
            if int(test[x]) - int(test[x-1]) >= int(test1[x]):
                count += 1
    print count

'''
Input:
2
3
1 10 15
1 10 3
3
10 20 30
15 5 20

Output:
2
1'''