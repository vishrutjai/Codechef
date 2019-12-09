a = input()
for x in range(a):
    s1 = raw_input()
    s2 = raw_input()
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i] and s1[i] != '?' and s2[i] != '?':

            count += 1

    count1 = 0
    for i in range(len(s1)):
        if s1[i] != s2[i] or (s1[i] == '?' and s2[i] == '?'):
            count1 += 1
    print count,count1





'''
Input:
3
a?c
??b
???a
???a
?abac
aba?w

Output:
1 3
0 3
3 5
'''

