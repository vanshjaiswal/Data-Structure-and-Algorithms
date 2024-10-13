"""
https://leetcode.com/problems/triangle/description/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
2
3 4
6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

"""

class Solution:
    def recursion(self, i, j, triangle):
        if i==len(triangle)-1:
            return triangle[i][j]
        
        diagonal = float("inf")
        down = triangle[i][j] + self.recursion(i+1, j, triangle)
        diagonal = triangle[i][j] + self.recursion(i+1, j+1, triangle)

        return min(down, diagonal)

    def memoization(self, i, j, triangle, dp):
        if i==len(triangle)-1:
            return triangle[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        diagonal = float("inf")
        down = triangle[i][j] + self.memoization(i+1, j, triangle, dp)
        diagonal = triangle[i][j] + self.memoization(i+1, j+1, triangle, dp)
        dp[i][j] = min(down, diagonal)

        return dp[i][j]
    
    def memoization_driver(self, triangle):
        n=len(triangle)
        dp = [[-1 for i in range(n)] for j in range(n)]

        output = self.memoization(0,0,triangle, dp)
        return output

    def tabulation(self, triangle):
        n=len(triangle)
        dp = [[-1 for i in range(n)] for j in range(n)]  
        #base case
        dp[n-1] = triangle[n-1]

        for i in range(n-2, -1, -1):
            for j in range(i,-1,-1):

                down = triangle[i][j] + dp[i+1][j]
                diagonal = triangle[i][j] + dp[i+1][j+1]

                dp[i][j] = min(down, diagonal)  

        return dp[0][0] 

    def space_optimized(self, triangle):
        front = triangle[-1]
        n=len(triangle)
        for i in range(n-2, -1, -1):
            temp = [0] * (i+1)
            for j in range(i, -1, -1):
                down = triangle[i][j] + front[j]
                diagonal = triangle[i][j] + front[j+1]
                temp[j] =  min(down, diagonal)

            front = temp

        return front[0]



        

sol = Solution()
# grid = [[2],[3,4],[6,5,7],[4,1,8,3]]
# grid=[[-1],[2,3],[1,-1,-3]]
grid = [[2],[3,4],[6,5,9],[4,4,8,0]]
n=len(grid)
# j=grid[n-1].index(min(grid[n-1]))

ans = sol.recursion(0, 0, grid)
print(ans)

ans = sol.memoization_driver(grid)
print(ans)

ans = sol.tabulation(grid)
print(ans)

ans = sol.space_optimized(grid)
print(ans)