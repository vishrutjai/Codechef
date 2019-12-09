l = []
z = input()
for a in range(z):
    l.append(input())
l.sort()
count = 0
for x in range(len(l)):
    temp = 0
    b = l[x]
    temp += (z-x) * b
    if temp > count:
        count = temp
print count

'''
Sample Input 1

4
30
20
53
14


Sample Output 1

60


Sample Input 2

5
40
3
65
33
21


Sample Output 2

99'''