"""
https://leetcode.com/problems/coin-change/description/

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 
"""

class Solution:

    def recursion(self, index, arr, target):
        
        if index == 0:
            if target % arr[0] == 0:
                return target//arr[0]
            else:
                return float("inf")

        not_take = 0 + self.recursion(index-1, arr, target)
        take = float("inf")
        if arr[index] <= target:
            #here we are adding 1 which signifies thta we are taking this coin
            #and incrementing the coin count by 1
            take = 1 + self.recursion(index, arr, target-arr[index])

        return min(take, not_take)

    def recursion_driver(self, coins, target):
        output = 0
        output = self.recursion(len(coins)-1, coins, target)
        if output == float("inf"):
            return -1
        else:
            return output

    def memoization(self, index, arr, target, dp):
        if index==0:
            if target % arr[0] == 0:
                return target // arr[0]
            else:
                return float("inf")

        if dp[index][target] != -1:
            return dp[index][target]
        
        not_take = 0 + self.memoization(index-1, arr, target, dp)
        take = float("inf")
        if arr[index] <= target:
            #here we are adding 1 which signifies thta we are taking this coin
            #and incrementing the coin count by 1
            take = 1 + self.memoization(index, arr, target-arr[index], dp)
        dp[index][target] = min(take, not_take)

        return dp[index][target]

    def memoization_driver(self, coins, amount):
        n=len(coins)

        dp=[[-1 for i in range(amount + 1)] for j in range(n)]

        output = self.memoization(n-1, coins, amount, dp)

        if output == float("inf"):
            return -1
        else:
            return output

    def tabulation(self, arr, amount):
        n=len(arr)

        dp=[[float("inf") for i in range(amount+1)] for j in range(n)]

        #base case:

        # if index==0:
        #     if target % arr[0] == 0:
        #         return target // arr[0]
        #     else:
        #         return float("inf")

        for i in range(amount+1):
            if i % arr[0] == 0:
                dp[0][i] = i // arr[0]

        #Write the for loop for the changing params

        for index in range(1, n):
            for target in range(amount + 1):
                not_take = 0 + dp[index-1][target]
                take = float("inf")
                if arr[index] <= target:
                    #here we are adding 1 which signifies thta we are taking this coin
                    #and incrementing the coin count by 1
                    take = 1 + dp[index][target-arr[index]]
                dp[index][target] = min(take, not_take)
        if dp[n-1][amount] != float("inf"):
            return dp[n-1][amount]
        else:
            return -1 

    def space_optimization(self, arr, amount):
        n=len(arr)

        prev = [float("inf")] * (amount + 1)

        for i in range(amount+1):
            if i % arr[0] == 0:
                prev[i] = i // arr[0]

        #Write the for loop for the changing params

        for index in range(1, n):
            temp = [float("inf")] * (amount + 1)
            for target in range(amount + 1):
                not_take = 0 + prev[target]
                take = float("inf")
                if arr[index] <= target:
                    take = 1 + temp[target-arr[index]]
                temp[target] = min(take, not_take)
            prev = temp
        if prev[amount] != float("inf"):
            return prev[amount]
        else:
            return -1 




sol = Solution()
coins = [1,2,5]
amount = 11

# coins = [2]
# amount = 3

# coins = [1]
# amount = 0

ans = sol.recursion_driver(coins, amount)
print(ans)

ans = sol.memoization_driver(coins, amount)
print(ans)

ans = sol.tabulation(coins, amount)
print(ans)

ans = sol.space_optimization(coins, amount)
print(ans)

        
