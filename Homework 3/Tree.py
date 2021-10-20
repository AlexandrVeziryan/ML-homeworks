def print_ls(ls):
    for i in ls:
        print(i, end="")
    print()    

n = int(input("Enter the Width of tree: "))
ls = []
for _ in range(n * 2 - 1):
    ls.append(" ")
point = n - 1
ls[point] = "*"
print_ls(ls)
shift = 2
for _ in  range(n // 2):
    ls[point + shift] = "*"
    ls[point - shift] = "*"
    shift += 2
    print_ls(ls)
    