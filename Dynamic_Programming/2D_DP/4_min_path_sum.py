"""
https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

"""

class Solution:
    def recursion(self, i, j, arr, up, left):
        if i==0 and j==0:
            return arr[0][0]
        if i<0 or j<0:
            return int(1e9)
        
        up = arr[i][j] +  self.recursion(i-1, j, arr, up, left)
      
        left = arr[i][j] + self.recursion(i, j-1, arr, up, left)

        return min(up, left)

    def memoization(self, i, j, arr, dp):
        
        if i==0 and j==0:
            return arr[0][0]
        if i<0 or j<0:
            return int(1e9)

        if dp[i][j] != -1:
            return dp[i][j]

        up = arr[i][j] +  self.memoization(i-1, j, arr, dp)
      
        left = arr[i][j] + self.memoization(i, j-1, arr, dp)

        dp[i][j] = min(left, up)

        return dp[i][j]

    def memoization_driver(self, grid):
        m=len(grid)
        n=len(grid[0])
        
        dp = [[-1 for i in range(n)] for j in range(m)]

        output  = self.memoization(m-1, n-1, grid, dp)
        return output



    def tabulation(self, arr):
        m=len(grid)
        n=len(grid[0])

        dp = [[-1 for i in range(n)] for j in range(m)]
        # print(dp)

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[0][0] = arr[0][0]
                    continue
                up= float("inf")
                left = float("inf")
                if i>0:
                    up = dp[i-1][j]
                if j>0:
                    left = dp[i][j-1]
            
                dp[i][j] = arr[i][j] + min(up, left)
        return dp[m-1][n-1]


    def space_optimized(self, grid):
        m=len(grid)
        n=len(grid[0])
        prev = [float("inf")] * n

        prev[0] = grid[0][0]

        for i in range(m):
            temp = [0] * n
            for j in range(n):
                if j==0 and i==0:
                    temp[j] = prev[j]
                    continue
                if j==0:
                    temp[j] = grid[i][j] + prev[j]
                    continue
                if j>0:
                    temp[j] = grid[i][j] + min(prev[j], temp[j-1])
            prev = temp

        return prev[n-1]




sol = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]

i=len(grid)
j=len(grid[0])

ans = sol.recursion(i-1, j-1, grid, 0, 0)
print(ans)

ans = sol.memoization_driver(grid)
print(ans)

ans = sol.tabulation(grid)
print(ans)

ans = sol.space_optimized(grid)
print(ans)