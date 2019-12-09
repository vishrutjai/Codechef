for i in range(input()):
    n = input()
    test = map(int,raw_input().split())
    test.sort()

    for x in test:
        print x,

'''
Input:
3
2
3 4
5
1 4 5 8 2
1
7

Output:
3 4
1 2 4 5 8
7
'''