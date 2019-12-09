a = input()
for x in range(a):
    str1 = raw_input()
    str2 = raw_input()
    if str1 == str2:
        print 'Yes'
    elif len(str1) == 1 and len(str2) == 1:
        if str1 == str2:
            print 'Yes'
        else:
            print 'No'
    else:
        flag = 0
        for x in range(1,len(str1)+1):
            if str1[0:x+1] in str2:
                flag = 1
                print 'Yes'
                break
            elif str1[0:x] in str2:
                print 'Yes'
                flag = 1
                break

        if flag != 1:
            print 'No'

