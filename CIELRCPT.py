
for y in range(input()):
    l = [2**x for x in range(12)]
    n = input()

    count = 0
    while n != 0:
        l1 = []
        m = 0
        for x in range(len(l)):
            if l[x] <= n:
                l1.append(l[x])
                m = x

        l = l[0:m+1]

        n -= l[-1]
        count +=1
    print count
'''
Sample Input

4
10
256
255
4096
Sample Output

2
1
8
2
'''