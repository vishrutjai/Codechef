def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

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


for a in range(input()):
    test = map(int,raw_input().split())
    print gcd(test[0],test[1]),lcm(test[0],test[1])
