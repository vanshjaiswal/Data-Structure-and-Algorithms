"""
https://leetcode.com/problems/edit-distance/description/

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""



class Solution:
    def recursion(self, i, j, s1, s2):
        #base case 

        if i<0:
            return j+1
        
        if j<0:
            return i+1

        if s1[i]==s2[j]:
            return 0 + self.recursion(i-1,j-1,s1,s2)

        else:
            return min(
                #insert
                1 + self.recursion(i, j-1, s1, s2),
                
                #delete
                1 + self.recursion(i-1, j, s1, s2),

                #replace
                1 + self.recursion(i-1, j-1, s1, s2)
                )

    def memoization(self, i, j, s1, s2,dp):
        #base case 

        if i<0:
            return j+1
        
        if j<0:
            return i+1

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i]==s2[j]:
            dp[i][j] = 0 + self.memoization(i-1,j-1,s1,s2,dp)
            return dp[i][j]

        else:

            dp[i][j] = min(
                #insert
                1 + self.memoization(i, j-1, s1, s2,dp),
                
                #delete
                1 + self.memoization(i-1, j, s1, s2,dp),

                #replace
                1 + self.memoization(i-1, j-1, s1, s2,dp)
                )
            return dp[i][j]

    def tabulation(self, s1, s2):
        n=len(s1)
        m=len(s2)

        dp = [[-1 for i in range(m+1)] for j in range(n+1)]

        #base case:

        # if i==0:
        #     return j
        
        # if j==0:
        #     return i
        
        for j in range(m+1):
            dp[0][j] = j

        for i in range(n+1):
            dp[i][0] = i

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = 0 + dp[i-1][j-1]

                else:
                    dp[i][j] =  min(
                        #insert
                        1 + dp[i][j-1],
                        
                        #delete
                        1 + dp[i-1][j],

                        #replace
                        1 + dp[i-1][j-1]
                        )
        return dp[n][m]

    def space_optimized(self, s1, s2):
        n=len(s1)
        m=len(s2)

        # dp = [[-1 for i in range(m+1)] for j in range(n+1)]
        prev = [0] * (m+1)
        
        for j in range(m+1):
            prev[j] = j

        # for i in range(n+1):
        #     dp[i][0] = i

        for i in range(1, n+1):
            cur = [0] * (m+1)
            cur[0] = i
            for j in range(1, m+1):
                if s1[i-1]==s2[j-1]:
                    cur[j] = 0 + prev[j-1]

                else:
                    cur[j] =  min(
                        #insert
                        1 + cur[j-1],
                        
                        #delete
                        1 + prev[j],

                        #replace
                        1 + prev[j-1]
                        )
            prev = cur
        return prev[m]


        
sol = Solution()
word1 = "intention" 
word2 = "execution"

n=len(word1)
m=len(word2)

dp = [[-1 for i in range(m)] for j in range(n)]

ans = sol.memoization(n-1, m-1, word1, word2,dp)
print(ans)

ans = sol.tabulation(word1, word2)
print(ans)

ans = sol.space_optimized(word1, word2)
print(ans)