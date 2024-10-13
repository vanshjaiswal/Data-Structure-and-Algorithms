"""
https://leetcode.com/problems/distinct-subsequences/description/

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit


This problem is the type of : STRING MATCHING IN DP



"""

class Solution:
    def recursion(self, i, j, str1, str2):
        #base case
        if j < 0:
            return 1
        if i < 0:
            return 0

        #match
        if str1[i] == str2[j]:
            #concept of recusrion all count (l+r)
            return (self.recursion(i-1, j-1, str1, str2) +  self.recursion(i-1, j, str1, str2))

        else:
            return self.recursion(i-1, j, str1, str2)

    def memoization(self, i, j, str1, str2,dp):
        #base case
        if j < 0:
            return 1
        if i < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        #match
        if str1[i] == str2[j]:
            #concept of recusrion all count (l+r)
            dp[i][j] = (self.memoization(i-1, j-1, str1, str2,dp) +  self.memoization(i-1, j, str1, str2,dp))
            return dp[i][j]

        else:
            dp[i][j] = self.memoization(i-1, j, str1, str2,dp)
            return dp[i][j] 

    def memoization_driver(self, s, t):
        n=len(s)
        m=len(t)
        dp = [[-1 for i in range(m)] for j in range(n)]
        return self.memoization(len(s)-1, len(t)-1, s, t,dp)

    def tabulation(self, str1, str2):
        n=len(str1)
        m=len(str2)

        dp=[[0 for i in range(m+1)] for j in range(n+1)]

        #base case:
        # if j < 0:
        #     return 1
        # if i < 0:
        #     return 0
        for j in range(m+1):
            dp[0][j] = 0

        for i in range(n+1):
            dp[i][0] = 1


        for i in range(1, n+1):
            for j in range(1, m+1):
                #match
                if str1[i-1] == str2[j-1]:
                    #concept of recusrion all count (l+r)
                    dp[i][j] =  (dp[i-1][j-1]) +  (dp[i-1][j])

                else:
                    dp[i][j] =  dp[i-1][j]

        return dp[n][m]






sol = Solution()
str1 = "rabbbit"
str2 = "rabbit"

ans  = sol.recursion(len(str1)-1, len(str2)-1, str1, str2)
print(ans)

ans  = sol.memoization_driver(str1,str2)
print(ans)

ans  = sol.tabulation(str1,str2)
print(ans)
