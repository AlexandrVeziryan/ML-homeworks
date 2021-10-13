n = int(input("Enter a number: "))
summ = 1
for i in range(1, n // 2 + 1):
    if n % i == 0:
        summ += 1
print(summ)

i = input()
