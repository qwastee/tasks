def is_palindrome(s):
    
    s = s.lower().replace(" ", "")
    
    return s == s[::-1]


string1 = "А роза упала на лапу Азора"
string2 = "Lukaku"
string3 = "mother"

print(is_palindrome(string1))
print(is_palindrome(string2)) 
print(is_palindrome(string3))


