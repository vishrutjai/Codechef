def merge(l1,l2):
    l3 = []
    p1 = 0
    p2 = 0
    m = len(l1)
    n = len(l2)
    while p1 < m and p2 < n:
        if l1[p1] < l2[p2]:
            l3.append(l1[p1])
            p1 += 1
        elif l1[p1] > l2[p2]:
            l3.append(l2[p2])
            p2 += 1
        else:
            l3.append(l1[p1])
            p1 += 1
            l3.append(l2[p2])
            p2 += 1
    while p1 < m:
        l3.append(l1[p1])
        p1 += 1
    while p2 < n:
        l3.append(l2[p2])
        p2 += 1
    return l3

def mergesort(l):
    i = 1
    while i <= len(l):
        j = 0
        l3 = []
        l7 = []
        while l3 != l:
            l1 = []
            l2 = []
            x = j
            while x < j + (i * 2) and x < len(l):
                # for x in range(j,j+(i*2)):
                # if x <= len(l):
                if x < j + i:
                    l1.append(l[x])
                else:
                    l2.append(l[x])
                # print(x)
                x += 1
            l4 = merge(l1, l2)
            # l[j:j+(i*2)] = l4
            l3 += l1 + l2
            l7 += l4
            # print(l3)
            # print(l1)
            # print(l2)
            j += (i * 2)
        l = l7[:]
        i *= 2
    return l

for ab in range(int(input())):
    l1 = [*map(int,input().split())]
    l2 = [*map(int,input().split())]
    l2 = mergesort(l2)
    t = (l1[1]+1)*(-1)
    #print(l2)
    while l2[t] == l2[t+1]:
        t -= 1
    print((-1)*(t+1))

'''Example Input
2
5 1
3 5 2 4 5
6 4
6 5 4 3 2 1
Example Output
2
4'''