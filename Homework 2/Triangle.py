a, b, c = int(input("Enter lenght of a: ")),int (input("Enter lenght of b: ")), int(input("Enter lenght of c: "))
maxx = max(a, b, c)
minn = min(a, b, c)
mid = maxx + minn - a - b - c

if a >= b + c or b >= a + c or c >= a + b:
    print("No Triangle")
elif minn ** 2 + mid ** 2  == maxx ** 2:
    print("Right Triangle")
elif minn ** 2 + mid ** 2  > maxx ** 2:
    print("Acute Triangle")
else:
    print("Obtuse Triangle")
i = input()
