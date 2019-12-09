a1 = input()
for i in range(a1):
    n = input()
    l = [x for x in range(5,n+1,5)]
    l1 = [y for y in range(25,n+1,25)]
    print int(len(l) + len(l1))


    #sum=1
    '''for x in range(1,n+1):
        sum*=x
    wow=str(sum)

    a=len(wow)-1

    c=0
    while wow[a]=='0':
        c+=1
        a-=1
    print int(c)'''

'''
Sample Input:

6
3
60
100
1024
23456
8735373
Sample Output:

0
14
24
253
5861
2183837'''