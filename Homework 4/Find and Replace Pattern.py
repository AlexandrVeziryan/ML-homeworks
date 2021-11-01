def Find_order(str):
    ls_lett = []
    ls_num = []
    for i in str:
        if not i in ls_lett:
            ls_lett.append(i)
        ls_num.append(ls_lett.index(i)) 
    return ls_num

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
res = []
order = Find_order(pattern)
for i in words:
    if Find_order(i) == order:
        res.append(i)
print(res)
