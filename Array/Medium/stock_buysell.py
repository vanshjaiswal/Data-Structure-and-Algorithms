"""
Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input:
 prices = [7,1,5,3,6,4]
Output:
 5
Explanation:
 Buy on day 2 (price = 1) and 
sell on day 5 (price = 6), profit = 6-1 = 5.
"""

#Brute force
def stock_buysell(nums):
    profit=0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            curr_profit = nums[j] - nums[i]
            if curr_profit > profit:
                profit = curr_profit
    
    return profit

# print(stock_buysell([7,1,5,3,6,4]))

#Optimal (self)
def stock_buysell1(nums):
    buy=0
    sell=1
    profit=0
    max_profit = float("-inf")
    for i in range(len(nums)):
        profit = nums[sell] - nums[buy]
        if profit > max_profit:
            max_profit = profit
        if profit < 0  and nums[sell] < nums[buy]:
            buy+=1
            sell+=1

    return max_profit
print(stock_buysell([7,1,5,3,6,4]))

def maxProfit(arr):
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro
        