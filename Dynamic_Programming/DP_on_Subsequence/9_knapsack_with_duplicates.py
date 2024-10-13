"""

https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=knapsack-with-duplicate-items

Input: N = 4, W = 8, val[] = {6, 1, 7, 7}, wt[] = {1, 3, 4, 5}
Output: 48
Explanation: The optimal choice is to pick the 1st element 8 times.

"""

class Solution:
    def recursion(self, index, W, val, wt):
        if index==0:
            if wt[0] <= W:
                return (W//wt[0]) * val[0]
            else:
                return float("-inf")

        
        take = float("-inf")
        if wt[index] <= W:
            take = val[index] + self.recursion(index, W-wt[index], val, wt)
        
        not_take = 0 + self.recursion(index-1, W, val, wt)
        return max(take, not_take)

    def memoization(self, index, W, val, wt,dp):
        if index==0:
            if wt[0] <= W:
                return (W//wt[0]) * val[0]
            else:
                return float("-inf")

        if dp[index][W] != -1:
            return dp[index][W]

        
        take = float("-inf")
        if wt[index] <= W:
            take = val[index] + self.memoization(index, W-wt[index], val, wt,dp)
        
        not_take = 0 + self.memoization(index-1, W, val, wt,dp)
        dp[index][W] = max(take, not_take)
        return dp[index][W]

    def memoization_driver(self, val, wt, W):
        n=len(wt)
        dp = [[-1 for i in range(W+1)] for j in range(n)]
        return self.memoization(n-1, W, val, wt,dp)


    def tabulation(self, val, wt, W):
        n=len(wt)
        dp = [[float("-inf") for i in range(W+1)] for j in range(n)]

        #base case
        # if index==0:
        #     if wt[0] <= W:
        #         return (W//wt[0]) * val[0]
        #     else:
        #         return float("-inf")

        for i in range(wt[0], W+1):
            dp[0][i] = val[0]
            



sol = Solution()
W = 8
val=[6, 1, 7, 7] 
wt= [1, 3, 4, 5]

ans = sol.recursion(len(wt)-1, W, val, wt)
print(ans)

ans = sol.memoization_driver(val, wt, W)
print(ans)