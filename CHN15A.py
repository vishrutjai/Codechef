for u in range(input()):
    test1 = map(int,raw_input().split())
    test2 = map(int,raw_input().split())
    count = 0
    for x in test2:
        x += test1[1]
        if x % 7 == 0:
            count +=1
    print count

'''
Input:
1
5 10
2 4 1 35 1

Output:
1'''