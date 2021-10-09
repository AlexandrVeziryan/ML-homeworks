def output(x, y):
    print(x, y)
    print(y, x)

x, y = int(input("Enter x: ")), int(input("Enter y: "))
x += 2
y -= 1
output(x, y)
output(x-4, y)
output(x, y+2)
output(x-4, y+2)
i = input()