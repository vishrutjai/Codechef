test = raw_input().split()
l1 = []
for x in range(int(test[0])):
    l1.append(input())
l2 = []
for y in range(int(test[1])):
    l2.append(input())
l3 = []
for z in range(int(test[2])):
    l3.append(input())
l4 = []
l4.append(l1)
l4.append(l2)
l4.append(l3)
l5 = []
j = 0
while j != len(l4):
    if l4[j] == l4[j+1] == l4[j+2]:
        l5.append(l4[j])
        j += 3
    elif l4[j] == l4[j+1]:
        l5.append(l4[j])
        j += 2



'''for i in l1:
    if i in l2 or i in l3:
        l4.append(i)
for j in l2:
    if j in l3 or j in l1:
        l4.append(j)
'''
'''for k in l3:
    if k in l1 or k in l2:
        l4.append(k)

l4.sort()
l5 = []
for i in l4:
    if i not in l5:
        l5.append(i)
'''
print len(l5)
for i in l5:
    print i


