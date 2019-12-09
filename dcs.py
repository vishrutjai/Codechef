l = ['ew','ui','tr','df','fd']
l1 = l[:]
s = ''
for x in l:
    s += x
    l1.remove(x)
print s
print l
print l1