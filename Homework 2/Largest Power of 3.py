N = int(input("Enter a number: "))
n = 3
if N < 3:
    if N == 1:
        print(1)
    else:
        print("Error")
else:
    while (n * 3) <= N:
        n *= 3
    print(n)
i = input()
