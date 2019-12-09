n = input()
d = {}
for x in range (n):
    temp = raw_input('Hour Time').split()
    d[temp[0]] = temp[1]
flag =0
for i in d:
    for j in d:
        if i == j and d[i] == d[j]:
            flag +=1
print flag
'''
1
7
10 20
5 40
10 20
23 11
5 50
10 30
17 12
'''





