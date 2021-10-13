n = int(input("Enter a number: "))
product = 1
while n > 0:
    last_num = n % 10
    n //= 10
    if last_num != 0:
        product *= last_num
print(product)
i = input()
