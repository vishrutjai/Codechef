import copy
a = input()
for hi in range(a):
    n = input()
    test = raw_input().split()
    count = int(test[0])
    if n == len(test):
        l2 = copy.deepcopy(test)
        l2.sort()
        count = int(l2[0])
        '''for x in range(len(test)):
            temp = 0
            for y in range(x,len(test)):
                temp += int(test[y])
            if temp > count:
                count = temp'''
        for x in range(1,len(test)-1):
            l1 = copy.deepcopy(test)
            l1.pop(x)
            tempcount = int(l1[x-1]) + int(l1[x])
            if tempcount > count:
                count = tempcount
        print count



'''
Input:
2
5
1 -2 3 -2 5
2
-1 -2

Output:
8
-1
'''