Array = [1,2,3,5,8,7,9,11]
Comp_arr = list(range(min(Array), max(Array) + 1))
res = []
for i in Comp_arr:
    if not i  in Array:
        res.append(i)
print(res)



