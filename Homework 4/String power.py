def Find_base_sequence(str):
    base_sequence = ""
    for i in str:
        if not i in base_sequence:
            base_sequence += i
        else:
            break
    return base_sequence        

s = "abcabcabcabcabcabcabcabcabcabc"
k = -5
if k > 0:
    print(s * k)
elif k < 0:
    k *= -1
    base_sequence = Find_base_sequence(s)
    dividor_index = len(s) // len(base_sequence)
    if dividor_index * base_sequence == s:
        if dividor_index % k == 0:
            print(dividor_index // k * base_sequence)
        else:
            print("undefined")    




