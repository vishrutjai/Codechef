for u in range(int(input())):
    n = input()
    test = [*map(int,input().split())]
    test.sort()
    flag = 0
    for x in range(len(test)-1):
        if test[x] == test[x + 1]:
            flag = 1
            break
    if flag ==1 :
        print ('NO')
    else:
        print ('YES')
