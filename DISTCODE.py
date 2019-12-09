for u in range(input()):
    string = raw_input()
    count = 0
    l = []

    for x in range(len(string) - 1):
        tempstr = ''
        tempstr += string[x] + string[x+1]
        if tempstr not in l:
            count +=1
            l.append(tempstr)
    print count

