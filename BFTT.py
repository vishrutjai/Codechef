for ab in range(int(input())):
    n = int(input())
    if n < 333:
        print(333)
    else:
        l = []
        n += 1
        while True:
            count = 0
            n1 = str(n)
            flag = 0
            for x in n1:
                if x == "3":
                    count += 1
                if count == 3:
                    print(int(n1))
                    flag = 1
                    break
            if flag == 1:
                break
            else:
                n += 1

'''Example Input
3
221
333
3002
Example Output
333
1333
3033'''