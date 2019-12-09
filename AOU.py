import math
'''def primechecker(num):
    flag = 0
    for i in range(2,num):
        if (num % i) == 0:
            flag += 1
    if flag == 0:
        return True
    else:
        return False'''
def print_factors(x,l):
   for i in range(1, x + 1):
       if x % i == 0:
           if i.isprime():
               l.append(i)
   print l
a=input('Test Cases')
for x in range(a):
    num = int(input("Enter a number: "))
    count = 0
    l=[]
    for i in range(1,num  + 1):
       if num % i == 0:
           if i.isprime():
               l.append(i)
    print l




