a= raw_input()
tempstr = ''
i = len(a)-1
while a[i] == ')':
    i-=1
while a[i] != '(':
    tempstr += a[i]
    i-=1
temp = ''
for x in range(len(tempstr)-1,-1,-1):
    temp += tempstr[x]
print temp