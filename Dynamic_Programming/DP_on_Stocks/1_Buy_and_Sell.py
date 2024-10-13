"""

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        max_profit = 0
        mini = prices[0]

        for i in range(1, n):
            cur_profit = prices[i] - mini
            max_profit = max(max_profit, cur_profit)
            mini = min(mini, prices[i])

        return max_profit

sol = Solution()
prices =[7,1,5,3,6,4]

print(sol.maxProfit(prices))