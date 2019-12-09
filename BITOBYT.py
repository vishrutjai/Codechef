for ab in range(int(input())):
    n = int(input())
    l = [1,0,0]
    i = 1
    while i < n:
        if i % 16 == 0:
            l[1] += (l[2]*2)
            l[2] = 0
        if i % 8 == 0:
            l[2] += l[1]
            l[1] = 0
        if i % 2 == 0:
            l[1] += l[0]
            l[0] = 0
        i += 1
        print(l)
    #print(l)
    for x in l:
        print(x,end=" ")

