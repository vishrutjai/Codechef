for hi in range(input()):
    n = input()
    l = [1,10,25,100,1000,2500,10000,100000,250000,1000000,25000000]
    count = 0
    while n!= 0:
        for x in range(len(l)-1,-1,-1):
            if n >= l[x]:

                n -= l[x]
                l = l[0:x+1]
                break
        count += 1
    print count
