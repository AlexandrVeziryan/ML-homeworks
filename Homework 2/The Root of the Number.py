def Find_root(n):
    print(n)
    root = 0
    while n > 0:
        root += n % 10
        n //= 10
    if root < 10:
        return root
    else:
        return Find_root(root)

n = int(input("Enter a number: "))
print(Find_root(n))
i = input()
