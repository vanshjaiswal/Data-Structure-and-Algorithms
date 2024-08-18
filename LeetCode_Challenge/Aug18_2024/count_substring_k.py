"""
You are given a binary string s and an integer k.

A binary string satisfies the k-constraint if either of the following conditions holds:

The number of 0's in the string is at most k.
The number of 1's in the string is at most k.
Return an integer denoting the number of 
substrings
 of s that satisfy the k-constraint.


 Input: s = "10101", k = 1

Output: 12

Explanation:

Every substring of s except the substrings "1010", "10101", and "0101" satisfies the k-constraint.


"""


def countKConstraintSubstrings(s, k):
    n=len(s)
    output=0

    for i in range(n):
        count_one=0
        count_zero=0
        end=i
        while count_one <=k and count_zero <=k and end<n:
            if s[end]=="1":
                count_one+=1
            else:
                count_zero+=1
            
            if count_zero <=k or count_one<=k:
                output +=1
            end+=1
            
    return output
print(countKConstraintSubstrings("0001111", 2))
# print(countKConstraintSubstrings("1010101", 2)) #[1][0][1][0][1]

def countKConstraintSubstrings2( s: str, k: int) -> int:
    n=len(s)
    output=n

    for i in range(n):
        count_one=0
        count_zero=0
        
        if s[i]=="1":
            count_one += 1
        else:
            count_zero += 1
        # print("i=",i)
        for j in range(i+1,n):
            if s[j]=="1":
                count_one+=1
            else:
                count_zero+=1
            
            if count_zero <=k or count_one<=k:
                output +=1
            
    return output

# print(countKConstraintSubstrings2("1010101", 2))
print(countKConstraintSubstrings2("0001111", 2))


def countKConstraintSubstrings3(s: str, k: int) -> int:
    total: int = 0
    ones = zeros = 0
    left: int = 0
    for right in range(len(s)):
        if s[right] == '1':
            ones += 1
        else: zeros += 1
        while ones > k and zeros > k:
            if s[left] == '1':
                ones -= 1
            else: zeros -= 1
            left += 1
        total += right - left + 1
    return total
print(countKConstraintSubstrings3("0001111", 2))

def substringWindows(s,k):
    total = 0
    zeros = 0
    ones = 0
    stringsBefore = [0]
    substringsWithStart = []
    endIndex = 0
    for startIndex in range(len(s)):
        while endIndex < len(s) and (zeros + (s[endIndex] == '0') <= k or ones + (s[endIndex] == '1') <= k):
            if s[endIndex] == '1':
                ones += 1
            if s[endIndex] == '0':
                zeros += 1
            endIndex += 1
        if s[startIndex] == '1':
            ones -= 1
        else:
            zeros -= 1
        substringsAtStartIndex = endIndex - startIndex
        total += substringsAtStartIndex
        substringsWithStart.append(substringsAtStartIndex)
        stringsBefore.append(total)
    return (stringsBefore, substringsWithStart, total)

# print(substringWindows("1010101", 2))
