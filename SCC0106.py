def isprime(num):
    l = []
    flag1 = 0
    for y in range(1,num):
        if num % y == 0:
            flag1 += 1
            l.append(y)

    if flag == 1:
        return l
    else:
        return False
def isprime1(num):
    l = []
    flag1 = 0
    for y in range(1,num):
        if num % y == 0:
            flag1 += 1
            l.append(y)

    if flag == 1:
        return l
    else:
        return False
wow = input()
for hi in range(wow):
    number = input()
    flag = 0
    for x in range(1,number):
        if number % x == 0:
            flag = 0
            break
        else:
            l1 = isprime(number)
            l2 = isprime1(x)
            if len(l1) == 1 and len(l2) == 1:
                flag +=1
            



    print flag+1

'''

1
2
3
4
5
'''
'''
1
1
2
2
4'''