a = input()
for x in range(a):
    test = raw_input().split()
    l = [i for i in range(1,int(test[1])+1)]
    count = 0
    for y in range(len(l)):
        for z in range(len(l)):
            if l[y] + l[z] == int(test[0]):
                count += 1
    if count >= 1:
        print count
    else:
        print -1

'''
Sample Input
4
5 4
4 9
9 2
4 1

Sample Output
4
-1
8
1
'''