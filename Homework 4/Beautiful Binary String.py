n = int(input("Enter the size of binary string: "))
b = input("Enter the binary string: ")
steps = 0
for i in range(n // 2):
    pos = b.find("010") + 2
    if pos != 1:
        b = b[:pos] + "1" + b[pos+1:]
        steps += 1
    else:
        break  
print(steps)      
