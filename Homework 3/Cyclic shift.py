N = int(input("Enter lenght of sequence: "))
k = int(input("Enter number of cuclic shifting: "))
ls = []
i = 1
while i <= N:
    ls.append(int(input(f"Enter the {i}th element of sequence: ")))
    i += 1
i = N - 1    
for _ in range(k):
    ls = [ls[i]] + ls[:i]
print(ls)
