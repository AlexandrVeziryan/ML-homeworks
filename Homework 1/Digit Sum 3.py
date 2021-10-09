num = int(input())
summ = 0
for i in range(3):
    summ += num % 10
    num //= 10
print(summ)

i = input()