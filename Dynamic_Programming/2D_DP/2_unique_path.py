"""
https://leetcode.com/problems/unique-paths/description/

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

"""

class Solution:
    def unique_path_recursion(self, i, j, m, n):
        if i==m-1 and j==n-1:
            return 1

        if i>m-1 or j>n-1:
            return 0


        if i >= 0 and j>=0 and i<m and j<n:
            down = self.unique_path_recursion(i+1, j, m, n)
            right = self.unique_path_recursion(i, j+1, m, n)

        return down + right


    def memoization(self, i, j, m, n, dp):
        if i==m-1 and j==n-1:
            return 1

        if i>m-1 or j>n-1:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if i >= 0 and j>=0 and i<m and j<n:
            down = self.memoization(i+1, j, m, n, dp) 
            right = self.memoization(i, j+1, m, n, dp) 
        dp[i][j] = down + right

        return dp[i][j]
    
    def memoization_driver(self, m, n):
        dp = [[-1 for i in range(n)] for j in range(m)]     
        output = self.memoization(0, 0, m, n, dp)
        return output


    def tabulation(self, m, n):
        dp = [[-1 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                    continue
                up = 0
                left = 0
                if i > 0:
                    up = dp[i-1][j]
                if  j>0:
                    left = dp[i][j-1]
                dp[i][j] = up + left

        return dp[m-1][n-1]

    def space_optimized(self, m, n):
        prev=[0] * n
        prev[0] = 1

        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if j==0:
                    temp[j] = prev[j] + 0
                if j>0:
                    temp[j] = prev[j] + temp[j-1]
            prev = temp
        return  prev[n-1]


sol = Solution()
m=3
n=7
ans = sol.unique_path_recursion(0,0, m, n)
print(ans)

ans = sol.memoization_driver(m, n)
print(ans)


ans = sol.tabulation(m, n)
print(ans)

ans = sol.space_optimized(m, n)
print(ans)