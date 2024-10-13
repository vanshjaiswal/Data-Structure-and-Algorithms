"""
https://leetcode.com/problems/shortest-palindrome/description/?envType=daily-question&envId=2024-09-20

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

"""




class Solution:
    def recursion(self, i, j, s1, s2):
        if i < 0 or j< 0 :
            return 0

        if s1[i] == s2[j] :
            return 1 + self.recursion(i-1, j-1, s1, s2)
        else:
            return 0 +  max(self.recursion(i-1, j, s1, s2), self.recursion(i, j-1, s1, s2))

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(r[i:]):
                return r[:i] + s
sol = Solution()
s1 = "aacecaaa"
s2  = s1[::-1]

s1 = "abcd"
s2  = s1[::-1]

s1= "abb"
s2  = s1[::-1]


"""

abb

"""

longest_matching = sol.recursion(len(s1)-1, len(s1)-1, s1, s2)

longest_palindrome = len(s1) - longest_matching

ans = s2[:longest_palindrome]+s1

print(longest_palindrome)
print(ans)
