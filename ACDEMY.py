wow = input()
for x in range (wow):

    a1 = input()-2
    a = raw_input().split()
    count = 2
    for x in range (a1):
        if int(a[x])+int(a[x+1]) == int(a[x+2]):
            count +=1
    print count

