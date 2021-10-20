def Is_Polindrome_2(n):
    if n < 1:
        return False
    lenn = 1
    i = 10
    while True:
        if n / i < 1:
            i /= 10
            break
        lenn += 1
        i *= 10     
    for _ in range(0, lenn // 2):
        if (n // i != n % 10):      
            return False
        n -= (n // i) * i
        n //= 10
        i /= 100
    return True    

def Is_Polindrome(n):
    rev_n = int(str(n)[::-1])
    return n == rev_n

a, b = int(input("Enter a: ")), int(input("Enter b: "))
for i in range(a, b + 1):
    if Is_Polindrome(i):
        print(i, end=" ")

for i in range(a, b + 1):
    if Is_Polindrome_2(i):
        print(i, end=" ") 
