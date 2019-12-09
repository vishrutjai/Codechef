for a in range(input()):
    test = map(int,raw_input().split())
    c = test[0] * test[1]
    if test[0] >= 1000:
       d = format(float(c * 90 / 100), '.6f')
    else:
        d = format(float(c), '.6f')
    print int(d)


'''
Example

Input

3
100 120
10 20
1200 20

Output

12000.000000
200.000000
21600.000000
'''