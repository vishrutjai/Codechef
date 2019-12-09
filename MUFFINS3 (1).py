a = input()
for hi in range(a):
    n = input()
    lorem = n

    for x in range(1,n+1):
        n1 = n % x
        print 'x',x
        print 'n1',n1
        print 'lorem',lorem
        if lorem >= n1:
            hipack = x
            lorem = n1
    print lorem



'''
Sample Input

2
2
5
Sample Output

2
3
'''