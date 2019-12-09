for a in range(int(input())):
    l = [*map(int,input().split())]
    l1 = []
    total = l[0] + l[1]
    '''if total % l[2] == 0:
        print("CHEF")
    else:
        print("COOK")'''
    '''i = 0
    j = -1
    while i < total+1:
        if (i) % l[2] == 0:
            #print(1)
            #print()
            j *= -1
        if j == 1:
            l1.append("CHEF")
        else:
            l1.append("COOK")
        i += 1'''
    #print(l1)
    #print(l1[total])
    #print(total//l[2])
    if (total/l[2]) % 2 == 0:
        print("CHEF")
    else:
        print("COOK")


'''3
1 3 2
0 3 2
34 55 2'''