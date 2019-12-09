a = input()
for x in range(a):
    test = raw_input().split()
    l = []
    for y in test:
        l.append(int(y))
    l.sort()
    print int(l[1])

'''
Input
3
120 11 400
10213 312 10
10 3 450

Output

120
312
10
'''