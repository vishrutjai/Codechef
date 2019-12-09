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

l1 = [*map(int,input().split())]
l2 = [*map(int,input().split())]
l3 = [*map(int,input().split())]
l4 = [l2[i]*l3[i] for i in range(len(l3))]

l = [l2[i]*l3[i] for i in range(len(l3))]
i = 1
while i <= len(l):
    j = 0
    l3 = []
    l7 = []
    while l3 != l:
        l1 = []
        l2 = []
        x = j
        while x < j+(i*2) and x < len(l):
        #for x in range(j,j+(i*2)):
            #if x <= len(l):
            if x < j+i:
                l1.append(l[x])
            else:
                l2.append(l[x])
            #print(x)
            x += 1
        l4 = merge(l1,l2)
        #l[j:j+(i*2)] = l4
        l3 += l1 + l2
        l7 += l4
        #print(l3)
        #print(l1)
        #print(l2)
        j += (i*2)
    l = l7[:]
    i *= 2

m = l1[1]
while m != 0:
    maxi = 0
    maxpos = 0
    for x in range(len(l4)):
        if l4[x] > maxi:
            maxi = l4[x]
            maxpos = x
    l4[maxpos] -= l3[maxpos]
    m -= 1


maxi = 0
maxpos = 0
for x in range(len(l4)):
        if l4[x] > maxi:
            maxi = l4[x]
            maxpos = x
print(maxi)
