l1 = ['A','D','O','P','Q','R']
l2 = ['B']
l3 = ['C','W','E','T','Y','U','I','S','F','G','H','J','K','L','Z','X','C','V','N','M']
for u in range(input()):
    string = raw_input()
    count = 0
    for x in string:
        if x in l1:
            count += 1
        elif x in l2:
            count += 2
    print count