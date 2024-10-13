"""
https://www.naukri.com/code360/problems/0-1-knapsack_920542?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos

W = [1, 2, 4, 5]
Value = [5, 4, 8, 6]
weight = 5
"""

class Solution:

    def recursion(self, index, w, weight, value):
        #base case: when we reach at index 0 then if the available weight in the knapsack
        # is greater than the weight of item at index 0 then we can pick it, else not

        if index == 0:
            if weight[0] <= w:
                return value[0]
            else:
                return 0

        not_take =  0 + self.recursion(index-1, w, weight, value)
        take=float("-inf")
        if weight[index] <= w:
            take = value[index] + self.recursion(index-1, w-weight[index], weight, value)

        return max(take, not_take)

    def memoization(self, index, w, weight, value, dp):
        if index == 0:
            if weight[0] <= w:
                return value[0]
            else:
                return 0

        if dp[index][w] != -1:
            return dp[index][w]

        not_take =  0 + self.recursion(index-1, w, weight, value)
        take=float("-inf")
        if weight[index] <= w:
            take = value[index] + self.recursion(index-1, w-weight[index], weight, value)
        dp[index][w] = max(take, not_take)   
        return  dp[index][w]

    def memoization_driver(self, weight, value, w):
        n = len(weight)
        dp = [[-1 for i in range(w+1)] for j in range(n)]

        output = self.memoization(n-1, w, weight, value, dp)

        return output

    def tabulation(self, weight, value, w):
        n=len(weight)
        dp = [[0 for i in range(w+1)] for j in range(n)]

        #base case: For every weight[0] <= w we can still value[0]

        for i in range(weight[0], w+1):
            dp[0][i] = value[0]

        #create nested for loops for the parameters in bottom up
        for index in range(1, n):
            for bag_weight in range(w+1):
                #copy the recursion
                not_take =  0 + dp[index-1][bag_weight]
                take=float("-inf")
                if weight[index] <= bag_weight:
                    take = value[index] + dp[index-1][bag_weight-weight[index]]

                dp[index][bag_weight] =  max(take, not_take)
        
        return dp[n-1][w]

    def space_optimization(self, weight, value, w):
        n=len(weight)
        prev= [0] * (w+1)

        for i in range(weight[0], w+1):
            prev[i] = value[0]

        for index in range(1, n):
            cur =[0] * (w+1)
            for bag_weight in range(w+1):
                #copy the recursion
                not_take =  0 + prev[bag_weight]
                take=float("-inf")
                if weight[index] <= bag_weight:
                    take = value[index] + prev[bag_weight-weight[index]]

                cur[bag_weight] =  max(take, not_take)
            prev = cur
        print(prev)
        return prev[w]






    
sol = Solution()
weight = [1, 2, 4, 5]
value = [5, 4, 8, 6]
w = 5
n=4

ans = sol.recursion(n-1, w, weight, value)
print(ans)

ans = sol.memoization_driver(weight, value, w)
print(ans)

ans = sol.space_optimization(weight, value, w)
print(ans)

[[0, 5, 5, 5, 5, 5], 
[9, 9, 5, 9, 9, 9], 
[13, 17, 17, 17, 17, 17], 
[23, 23, 23, 23, 23, 19]]