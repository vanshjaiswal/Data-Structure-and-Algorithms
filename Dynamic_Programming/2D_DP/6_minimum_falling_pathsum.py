"""
https://leetcode.com/problems/minimum-falling-path-sum/description/
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
"""

class Solution:
    def recursion(self, i, j, matrix):
        if j<0 or j>=len(matrix):
            return float("inf")
        if i==0:
            return matrix[0][j]

        left = matrix[i][j] +  self.recursion(i-1, j-1, matrix)
        up = matrix[i][j] +  self.recursion(i-1, j, matrix)
        right = matrix[i][j] +  self.recursion(i-1, j+1, matrix)

        return min(left, right, up)

    def recursion_driver(self, matrix, n):
        #solving from n-1 to 0 row
        mini = float("inf")
        for j in range(n):
            value = self.recursion(n-1, j, matrix)
            mini = min(mini, value)
        return mini

    def memoization(self,i, j, matrix, dp):
        if j<0 or j>=len(matrix):
            return float("inf")
        if i==0:
            return matrix[0][j]

        if dp[i][j] != -1:
            return dp[i][j]

        left = matrix[i][j] +  self.memoization(i-1, j-1, matrix,dp)
        up = matrix[i][j] +  self.memoization(i-1, j, matrix,dp)
        right = matrix[i][j] +  self.memoization(i-1, j+1, matrix,dp)

        dp[i][j] = min(left, right, up) 

        return dp[i][j]
    
    def memoization_driver(self, matrix):
        n=len(matrix)
        dp = [[-1 for i in range(n)] for j in range(n)]

        mini = float("inf")

        for j in range(n):
            value = self.memoization(n-1, j, matrix, dp)
            mini = min(mini, value)
        return mini

    def tabulation(self, matrix):
        n =  len(matrix)
        dp =  [[0 for i in range(n)] for j in range(n)]
        
        #base  case
        dp[0] = matrix[0]

        for i in range(1, n):
            for j in range(n):
                up = matrix[i][j] +  dp[i-1][j]
                left = matrix[i][j]
                if j-1 >= 0:
                    left +=  dp[i-1][j-1]
                else:
                    left = float("inf")
                right= matrix[i][j]
                if j+1<n:
                    right +=  dp[i-1][j+1]
                else:
                    right =  float("inf")

                dp[i][j] =  min(up, left, right)
        
        return min(dp[n-1])

    def space_optimization(self, matrix):
        prev = matrix[0]
        n=len(matrix)
        for i in range(1, n):
            temp = [0] * n
            for j in range(n):
                if j==0:
                    temp[j] = matrix[i][j] + min(prev[j], prev[j+1])
                    continue
                if j>0 and j<n-1:
                    temp[j] = matrix[i][j] + min(prev[j-1], prev[j], prev[j+1])
                    continue
                if j<n:
                    temp[j] = matrix[i][j] + min(prev[j-1], prev[j])
                    
                
            prev = temp

        return min(prev)




sol = Solution()
matrix = [[2,1,3],[6,5,4],[7,8,9]]
n=len(matrix)
ans = sol.recursion_driver(matrix,n)
print(ans)

ans = sol.memoization_driver(matrix)
print(ans)

ans = sol.tabulation(matrix)
print(ans)

ans = sol.space_optimization(matrix)
print(ans)
