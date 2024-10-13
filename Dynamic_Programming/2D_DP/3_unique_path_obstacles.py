"""
https://leetcode.com/problems/unique-paths-ii/description/

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

class Solution:
    def recursion(self, i, j, arr):
        if i==0 and j==0:
            return 1

        if arr[i][j]==1:
            return 0

        if i<0 or j<0:
            return 0

        up = self.recursion(i-1, j, arr)

        left = self. recursion(i, j-1, arr)

        return up + left

    def memoization(self, i, j, arr, dp):
        if i==0 and j==0:
            return 1

        if arr[i][j]==1:
            return 0

        if i<0 or j<0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        up = self.recursion(i-1, j, arr)

        left = self. recursion(i, j-1, arr)

        dp[i][j] = up + left

        return dp[i][j]

    def memoization_driver(self, m, n, arr):
        dp=[[-1 for i in range(n)] for j in range(m)]
        output = self.memoization(m-1, n-1, arr, dp)
        return output

    def tabulation(self, m, n, arr): #bottoms up
        dp = [[-1 for i in range(n)] for j in range(m)]
        #base case
    
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                    continue
                up=0
                left=0
                if arr[i][j] != 1:
                    if i>0:
                        up = dp[i-1][j]
                    if j>0:
                        left= dp[i][j-1]
                dp[i][j] = up + left
        return dp[m-1][n-1]

    def space_optimized(self, m, n, arr):
        prev = [0] * n
        prev[0] = 1

        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if arr[i][j] != 1:
                    if j==0:
                        temp[j] = prev[j]
                        continue
                    if j>0:
                        temp[j] = prev[j] + temp[j-1]
            prev = temp

        return prev[n-1]



        
        
        

sol = Solution()

obstacleGrid =  [[0,0,0],[0,1,0],[0,0,0]]
i=len(obstacleGrid)
j=len(obstacleGrid[0])

ans = sol.recursion(i-1, j-1, obstacleGrid)
print(ans)

ans = sol.tabulation(i, j, obstacleGrid)
print(ans)

ans = sol.space_optimized(i, j, obstacleGrid)
print(ans)