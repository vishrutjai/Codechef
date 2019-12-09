n=raw_input().split()
cost = raw_input().split()

for x in range(int(n[1])):
    totalcost = 0
    case = raw_input().split()
    i = 0
    while i!=int(case[0])-1:
        totalcost += int(cost[i])
        i+=1
    i = int(case[1])

    while i != len(cost):
        totalcost += int(cost[i])
        i+=1
    print totalcost



