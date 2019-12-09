a = input()
for i in range(a):
    wow = input()
    wow1 = float(input())
    #test = raw_input().split()
    if float(wow1)<float(wow):
        print int(str(wow1)+'0')

    elif wow % 5 == 0:
        x = wow1 - (wow) - 0.5
        x = str(x)
        print int(x + '00')

    else:
        print (wow1)