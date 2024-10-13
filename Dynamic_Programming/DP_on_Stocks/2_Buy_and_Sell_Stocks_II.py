"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""

class Solution:
    def recursion(self, ind, buy, prices):
        if ind == len(prices):
            return 0

        if buy==0:
            op1 = 0 + self.recursion(ind+1, 0, prices)
            op2 = -prices[ind] + self.recursion(ind + 1, 1, prices)
        
        else:
            op1 = 0 + self.recursion(ind+1, 1, prices)
            op2 = prices[ind] + self.recursion(ind + 1, 0, prices)

        return max(op1, op2)
        
    def memoization(self, ind, buy, prices, dp):
        if ind == len(prices):
            return 0

        if dp[ind][buy] != -1:
            return dp[ind][buy]

        if buy==0:
            op1 = 0 + self.memoization(ind+1, 0, prices, dp)
            op2 = -prices[ind] + self.memoization(ind + 1, 1, prices, dp)
        
        else:
            op1 = 0 + self.memoization(ind+1, 1, prices, dp)
            op2 = prices[ind] + self.memoization(ind + 1, 0, prices, dp)

        dp[ind][buy] = max(op1, op2)
        return dp[ind][buy]


    def tabulation(self, prices):
        n=len(prices)

        dp = [[-1 for i in range(2)] for j in range(len(prices)+1)]

        #base case 
        # if ind == len(prices):
        #     return 0
        dp[n][0] = 0
        dp[n][1] = 0

        for ind in range(n-1, -1, -1):
            for buy in range(2):
                if buy==0:
                    op1 = 0 + dp[ind+1][0]
                    op2 = -prices[ind] + dp[ind + 1][1]
                
                else:
                    op1 =  0 + dp[ind+1][1]
                    op2 = prices[ind] + dp[ind + 1][0]
                dp[ind][buy] = max(op1, op2)

        return dp[ind][0]

    def space_optimized(self, prices):
        n=len(prices)
        prev=[0, 0]

        for ind in range(n-1, -1, -1):
            curr = [0, 0]
            for buy in range(2):
                if buy==0:
                    op1 = 0 + prev[0]
                    op2 = -prices[ind] + prev[1]
                
                else:
                    op1 =  0 + prev[1]
                    op2 = prices[ind] + prev[0]

                curr[buy] = max(op1, op2)
            prev = curr

        return prev[0]






sol = Solution()
# prices = [7,1,5,3,6,4]
prices=[1,2,3,4,5]
# ans = sol.recursion(0,0,prices)
# print(ans)

# dp = [[-1 for i in range(2)] for j in range(len(prices)+1)]
# ans = sol.memoization(0,0,prices,dp)
# print(ans)


ans= sol.tabulation(prices)
print(ans)

ans= sol.space_optimized(prices)
print(ans)
