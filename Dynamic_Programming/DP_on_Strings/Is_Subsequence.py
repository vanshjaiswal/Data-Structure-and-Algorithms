"""
https://leetcode.com/problems/is-subsequence/description/

"""

class Solution:

    def recursion(self, i, t, j, s):
        if j<0:
            return True
        if i<0:
            return False

        if s[j] == t[i]:
            return self.recursion(i-1, t, j-1, s)
        else:
            return self.recursion(i-1, t, j, s)



    def isSubsequence(self, s: str, t: str) -> bool:
        return self.recursion(len(t)-1, t, len(s)-1, s)
        