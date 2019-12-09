for i in range(input()):
    n = input()
    test = map(int,raw_input().split())
    test1 = test[1:len(test)]
    count = 0
    for x in test1:
        if x >= test[0]:
            count += 1
    print count
'''
Example

Input:
2
4
1 2 3 4 5
5
1 10 100 1000 10000 100000

Output:
4
5'''