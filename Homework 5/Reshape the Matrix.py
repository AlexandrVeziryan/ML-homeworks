mat = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
r = 8
c = 2
if r * c != len(mat) ** 2:
    print(mat)
else:
    mat_2 = []
    for i in mat:
        mat_2.extend(i)
    res = []
    elem = 0
    for i in range(r):
        res.append([])
        for j in range(c):
            res[i].append(mat_2[elem])
            elem += 1
    print(res)


