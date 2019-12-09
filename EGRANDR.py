for  x in range(input()):
    n = input()
    test = map(int,raw_input().split())
    if 2 in test:
        print 'No'
    elif 5 in test:
        count = 0.0
        for y in test:
            count += y
        count /= n
        if count >= 4.0:
            print 'Yes'
        else:
            print 'No'

