a= input()
for x in range(a):
    n = input()
    test = raw_input().split()
    count = 100000000000
    for i in range(n):
        for j in range(i+1,n):

            if int(test[i]) + int(test[j]) < count:
                count = int(test[i]) + int(test[j])
    print count

'''
Input:
1
4
5 1 3 4

Output:
4
'''