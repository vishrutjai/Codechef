for u in range(input()):
    n = raw_input()
    l = []
    for x in n:
        l.append(x)
    l.sort()
    count = 0
    flag = 0
    l3 = []
    for x in l:
        l1 = l[:]
        l1.remove(x)
        for y in l1:
            l2 = l[:]
            l2.remove(x)
            l2.remove(y)
            for z in l2:
                count += 1

                string = x + y + z
                if string == n:
                    flag = 1
                    print count
                    break
                if flag == 1:
                    break
            if flag == 1:
                break
        if flag == 1:
            break
                #l3.append(string)
    '''for x in range(len(l3)):
        if n == l3[x]:
            print x + 1
            break'''
'''
Input:
2
276
762

Output:
2
6'''