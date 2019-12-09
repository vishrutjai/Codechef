for u in range(input()):
    n = input()
    test = map(int,raw_input().split())
    test.sort()
    count = 0
    l = []
    for x in range(len(test)):
        if test[x] not in l:
            l.append(test[x])
    print len(l)
