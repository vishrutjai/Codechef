for u in range(input()):
    test = map(int,raw_input().split())
    if test[0] > test[1]:
        print '>'
    elif test[0] < test[1]:
        print '<'
    else:
        print '='