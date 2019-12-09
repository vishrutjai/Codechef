string = raw_input()
flag1 = flag2 = flag3 = flag4 = 0
count = 0
count1 = 0
for x in string:
    if x.isalpha() == True:
        count += 1
    if count == 5:

        flag1 = 1
    if x.isdigit() == True:

        flag2 = 1
    elif x.isupper() == True:

        flag3 = 1
    elif x.islower() == True:

        flag4 = 1
    if flag1 == 1 and flag2 == 1 and flag3 == 1 and flag4 == 1:

        count1 = 4
        break
if count1 != 4:
    print 'NO'



'''
Example

Input:
abcdefgh

Output:
NO



Input:
SPIT_Coders_Club_2.0

Output:
YES'''
