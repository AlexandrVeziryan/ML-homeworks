logs = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k = 5
logs.sort()
ls_k = []
for i in range(k):
    ls_k.append(0)
IDs = [logs[0][0]]
for i in range(1, len(logs)):
    if not logs[i][0] in IDs:
        IDs.append(logs[i][0]) 
i = 0
logs_size = len(logs)
for ID in IDs:
    ls_times = []
    while i < logs_size:
        if logs[i][0] == ID:
            if not logs[i][1] in ls_times:
                ls_times.append(logs[i][1])
            i += 1    
        else:

            break    
    ls_k[len(ls_times) - 1] += 1
print(ls_k)    
            







