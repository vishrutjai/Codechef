for i in range(input()):
    test1 = map(int,raw_input().split())
    test2 = map(int,raw_input().split())
    test2.sort(reverse=True)
    test3 = test2[test1[1]:len(test2)]

    count = 0
    for x in test3:
        count += x
    print count

'''
Example

Input:
2
5 3
1 1 1 1 1
2 1
3 4
Output:
2
3'''

