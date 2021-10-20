ls = []
i = 1
while True:
    n = input(f"Enter the {i}th element of sequence: ")
    if not n:
        break
    i += 1
    ls.append(float(n))
ls2 = []
print(ls)
for i in range(len(ls)):
    ls2.append(sum(ls[i:]))
print(ls2)
