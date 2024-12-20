def palindrome(str):
    s_list=list(str)
    s_list.reverse()
    rev=''.join(s_list)
    if str==rev:
        return "Palindrome"
    return "Not palindrome"
str=input("Enter string")
print(palindrome(str))