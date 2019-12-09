test = raw_input().split()
count = 0
for x in range(int(test[0])):
    n = input()
    if n % 4 == 0:
        count += 1
print count
