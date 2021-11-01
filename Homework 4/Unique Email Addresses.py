def Is_actual_email(str):
    str2 = ""
    for i in range(len(str)):
        if str[i] == "@":
            str2 += str[i:]
            break
        elif str[i] == "+":
            break
        elif str[i] == ".":
            continue
        else:
            str2 += str[i]
    if not "@" in str2:    
            str2 += str[str.find("@"):]   
    return str2        

emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
actual_emails = []
for i in emails:
    actual_email = Is_actual_email(i)
    if not actual_email in actual_emails:
        actual_emails.append(actual_email)
    print(actual_emails)        
print(len(actual_emails))        
