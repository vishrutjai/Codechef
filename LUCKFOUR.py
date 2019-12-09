a = input()
for x in range(a):
    n = str(input())
    count = 0
    for y in n:
        if int(y) == 4:
            count += 1
    print count
