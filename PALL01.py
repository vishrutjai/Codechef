a = input()
for x in range(a):
    n = str(input())
    str1 = ''
    for i in range(len(n)-1,-1,-1):
        str1 += n[i]
    if str1 == n:
        print 'wins'
    else:
        print 'losses'

