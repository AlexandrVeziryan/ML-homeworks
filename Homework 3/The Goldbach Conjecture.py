def Is_prime(n):
    is_prime = True
    for i in range(2, n//2 + 1):
        if n % i == 0:
            is_prime = False
    return is_prime

n = int(input())
if Is_prime(n):
    print("Error")
else:    
    num = n // 2 + 1
    i = 2
    while i < num:
        if Is_prime(i) and Is_prime(n - i):
            print(i,  n - i)
            break
        i += 1
