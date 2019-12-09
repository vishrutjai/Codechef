def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

a = input()
for hi in range(a):
    test = raw_input().split()
    a = int(test[0])
    b = int(test[1])
    c = int(test[2])
    d = int(test[3])
    q = lcm(a,b)
    if c == d and a != b:
        print 1

