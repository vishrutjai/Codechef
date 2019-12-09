def palindrome(n):
    string = str(n)
    a = string[::-1]
    if string == a:
        return True
    else:
        return False
def isprime(n):
    flag = 0
    for x in range(2,n):
        if n % x == 0:
            flag += 1
    if flag != 0:
        return True
    else:
        return False

n = input()
while True:#palindrome(n) == False and isprime(n) == False:
    h = palindrome(n)
    i = isprime(n)
    if h == False and i == False:
        break
    else:
        n += 1
print n