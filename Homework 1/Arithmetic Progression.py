a, b, n = int(input()), int(input()), int(input())
for i in range(3, n + 1):
    a, b = b, b - (a - b)# or 2b - a
print(b)
i = input()    


