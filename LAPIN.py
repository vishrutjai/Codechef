a = input()
for i in range(a):
    string = raw_input()
    if len(string)%2 ==0:
        str1 = string[0:(len(string)/2)]
        str2 = string[(len(string)/2):len(string)]

        l1 = []
        l2 = []
        for x in str1:
            l1.append(x)
        for x in str2:
            l2.append(x)
        l2.sort()
        l1.sort()
        if l1 == l2:
            print 'YES'
        else:
            print 'NO'
    else:
        l3 = []
        string1 = ''
        for x in string:
            l3.append(x)
        l3.pop(len(l3)/2)

        for x in l3:
            string1 += x
        str1 = string1[0:(len(string1)/2)]
        str2 = string1[(len(string1)/2):len(string1)]
        l1 = []
        l2 = []
        for x in str1:
            l1.append(x)
        for x in str2:
            l2.append(x)
        l2.sort()
        l1.sort()
        if l1 == l2:
            print 'YES'
        else:
            print 'NO'

