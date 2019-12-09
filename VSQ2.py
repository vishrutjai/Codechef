import random
n=input('Number')
l1 = [x for x in range(n)]
l2 = [x for x in range(n)]
d = {}
temp = 0
for i in range(n*10):
    for j in l1:
        tempdict = {}
        tempdict[j] = random.choice(l2)

