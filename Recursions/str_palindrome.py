import re
def palindrome(s):
    s=s.lower()
    s=re.sub("[^a-z]","",s)
    if s==s[::-1]:
        return True
    else:
        return False

# print(palindrome("0P"))


#recursions
def palindrome_recursive(s, start, end):
    if start==end:
        return True

    if s[start]==s[end]:
        return palindrome_recursive(s, start+1, end-1)
    else:
        return False
s="0P"
s=s.lower()
s=re.sub("[^a-z]","",s)
print(palindrome_recursive(s, 0, len(s)-1))