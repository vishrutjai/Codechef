test = map(int,raw_input().split())
while test != [0,0,0]:
    if test[1] - test[0] == test[2] - test[1]:
        d = test[1] - test[0]
        print 'AP',test[2] + d
    elif test[1] / test[0] == test[2] / test[1]:
        r = test[1] / test[0]
        print'GP',test[2] * r
    test = map(int,raw_input().split())
'''
Input:
4 7 10
2 6 18
0 0 0
Output:
AP 13
GP 54'''