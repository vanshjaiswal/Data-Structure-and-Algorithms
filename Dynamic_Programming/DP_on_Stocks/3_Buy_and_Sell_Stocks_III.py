"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

cap= 2

max two transactions you can do 


"""


class Solution:
    def recursion(self, ind, buy, cap, prices):
        if cap==0:
            return 0
        if ind==len(prices):
            return 0

        if buy==0:
            op1 = 0 + self.recursion(ind+1, 0, cap, prices)
            op2 = -prices[ind] +  self.recursion(ind+1, 1, cap, prices)
        else:
            op1 = 0 + self.recursion(ind+1, 1, cap, prices)
            op2 = prices[ind] +  self.recursion(ind+1, 0, cap-1, prices) 

        return max(op1, op2) 

    def memoization_driver(self, prices):
        n=len(prices)
        cap=2
        #here we have 3 changing params so we need a 3d dp

        #ind= 0 --> n-1
        #buy = 0 or 1
        #cap = 0,1,2
        #dp = [N][buy][cap]

        dp=[[[-1 for i in range(cap+1)] for j in range(2)] for k in range(n+1)]

        return self.memoization(0, 0, 2, prices,dp)

    def memoization(self, ind, buy, cap, prices,dp):
        if cap==0:
            return 0
        if ind==len(prices):
            return 0

        if dp[ind][buy][cap] != -1:
            return dp[ind][buy][cap]

        if buy==0:
            op1 = 0 + self.memoization(ind+1, 0, cap, prices,dp)
            op2 = -prices[ind] +  self.memoization(ind+1, 1, cap, prices,dp)
        else:
            op1 = 0 + self.memoization(ind+1, 1, cap, prices,dp)
            op2 = prices[ind] +  self.memoization(ind+1, 0, cap-1, prices,dp) 

        dp[ind][buy][cap] = max(op1, op2)

        return dp[ind][buy][cap]

    def tabulation(self, prices):
        n = len(prices)
        
        # Create a 3D DP table with dimensions (n+1) x 2 x 3 and initialize it to 0 values
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
        
        # The base case is already covered as the DP array is initialized to 0
        
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    
                    if buy == 0:
                        # We can buy the stock
                        dp[ind][buy][cap] = max(0 + dp[ind + 1][0][cap], -prices[ind] + dp[ind + 1][1][cap])
                    elif buy == 1:
                        # We can sell the stock
                        dp[ind][buy][cap] = max(0 + dp[ind + 1][1][cap], prices[ind] + dp[ind + 1][0][cap - 1])
        
        return dp[0][0][2]



sol = Solution()
prices=[3,3,5,0,0,3,1,4]
# ans = sol.recursion(0,0,2,prices)
# print(ans)

# ans = sol.memoization_driver(prices)
# print(ans)

ans= sol.tabulation(prices)
print(ans)
# print(dp)

# [[[13, 13, 13], [19, 19, 19]], 
# [[10, 10, 10], [16, 16, 16]], 
# [[8, 8, 8], [13, 13, 13]], 
# [[8, 8, 8], [8, 8, 8]], 
# [[8, 8, 8], [8, 8, 8]], 
# [[3, 3, 3], [8, 8, 8]], 
# [[3, 3, 3], [5, 5, 5]], 
# [[0, 0, 0], [4, 4, 4]], 
# [[0, 0, 0], [0, 0, 0]]]