for u in range(input()):
    test = raw_input().split()
    test[0].sort()
    test[1].sort()
    if test[0] == test[1]:
        print 'YES'
    else:
        print 'NO'