a = input()
for hi in range(a):
    n = raw_input().split()
    test = raw_input().split()
    test.sort()
    for x in range(int(n[1])):
        test.pop(x)
    test.sort(reverse=True)
    for x in range(int(n[1])):
        test.pop(x)
    count = 0
    for x in test:
        count += int(x)
    count = count len(test)
    count1 = str(count)
    while len(count1) != 8:
        count1 += '0'
    print int(count1)

