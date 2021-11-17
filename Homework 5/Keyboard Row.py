def is_used_one_row(word, key):
    for i in word:
        if not i in key:
            return False
    return True        

words = ["Hello","Alaska","Dad","Peace"]
keys = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
res = []
for wordd in words:
    word = wordd.lower()
    is_used = False
    if word[0] in keys[0] and is_used_one_row(word, keys[0]):
        is_used = True
    elif word[0] in keys[1] and is_used_one_row(word, keys[1]):
        is_used = True
    elif(is_used_one_row(word, keys[2])):
        is_used = True
    if is_used:
        res.append(wordd)    
print(res)
        




    
