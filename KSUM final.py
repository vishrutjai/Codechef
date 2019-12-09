
temp = raw_input().split()
l= raw_input().split()
k = int(temp[1])
l.sort()
print l
count = 0
wow = len(l)
highcount = 0
i = 0
if int(temp[0]) >= int(temp[1]):


    while k != 0:

        count = 0
        for x in range(i,len(l)):
            count += int(l[x])
        i += 1

        print count,
        k -= 1
else:
    '''bigl = []
    bigl.append(l)
    for x in l:
        bigl.append(x)
    for y in range(len(l)-1,-1,-1):
        templ = []
        templ.append(l[y])
        templ.append(l[y-1])
        bigl.append(templ)
    print bigl'''
    bigl = []
    bigl.append(l)
    for x in l:
        bigl.append(x)
    for x in range (len(l)):
        templ = []
        for y in range(x):

            templ.append(l[x])
            templ.append(l[y])
        bigl.append(templ)
    print bigl






