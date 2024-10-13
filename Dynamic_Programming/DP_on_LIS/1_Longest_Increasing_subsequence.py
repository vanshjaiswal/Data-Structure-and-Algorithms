"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

In this problem we are going to use the pick/not_pick concept 
but we have to track the previous element and we can only pick when the current element
is greater than the previous on.

f(ind, prev_ind)


EXPLORE THE BINARY SEARCH SOLUTION
"""



class Solution:
    def recursion(self, ind, prev_ind, arr):
        if ind==len(arr):
            return 0

        not_take = 0 + self.recursion(ind+1, prev_ind, arr)
        take = float("-inf")
        if prev_ind == -1 or arr[ind] > arr[prev_ind]:
            take = 1 + self.recursion(ind+1, ind, arr)

        return max(take, not_take)

    def memoization(self, ind, prev_ind, arr, dp):
        if ind==len(arr):
            return 0
        #since we have -1 value for the prev so we will use the 1 based indexing
        #for the prev_ind and we also create a dp [n][n+1]
        if dp[ind][prev_ind+1] != -1:
            return dp[ind][prev_ind+1]

        not_take = 0 + self.memoization(ind+1, prev_ind, arr, dp)
        take = float("-inf")
        if prev_ind == -1 or arr[ind] > arr[prev_ind]:
            take = 1 + self.memoization(ind+1, ind, arr, dp)
        dp[ind][prev_ind+1] = max(take, not_take)

        return dp[ind][prev_ind+1]
    
    def tabulation(self, arr):
        n = len(arr)

        dp = [[0 for i in range(n+1)] for j in range(n+1)]

        for ind in range(n-1, -1, -1):
            for prev_ind in range(ind-1, -2, -1):
                not_take = 0 + dp[ind+1][prev_ind+1]
                take = float("-inf")
                if prev_ind == -1 or arr[ind] > arr[prev_ind]:
                    take = 1 + dp[ind+1][ind+1]

                dp[ind][prev_ind+1] =  max(take, not_take)
        return dp[0][0]

    def tabulation2(self, arr):
        n=len(arr)
        dp = [1] * (n)

        for ind in range(n):
            for prev in range(0, ind):
                if arr[prev] < arr[ind]:
                    dp[ind] = max(1 + dp[prev], dp[ind])
        return max(dp)

    def print_lis(self, arr):
        n=len(arr)
        dp = [1] * (n)
        hash = [0] * (n)

        for ind in range(n):
            hash[ind] = ind
            for prev in range(0, ind):
                if arr[prev] < arr[ind] and (1+dp[prev] > dp[ind]):
                    dp[ind] = 1 + dp[prev]
                    hash[ind] = prev

        # print("HASH---", hash)
        # print("DP-----",dp)
        # print("Arr----", arr)

        #find the max value in dp and its index
        ans = max(dp)
        last_index = dp.index(ans)

        # print(last_index)
        temp = [arr[last_index]]

        while hash[last_index] != last_index:
            last_index = hash[last_index]
            temp.append(arr[last_index])



        return temp[::-1]



sol = Solution()
# arr = [10,9,2,5,3,7,101,18]
# print(sol.recursion(0, -1, arr))

# dp = [[-1 for i in range(len(arr) + 1)] for j in range(len(arr))]
# print(sol.memoization(0, -1, arr, dp))

# print(sol.tabulation2(arr))


arr= [5,4,11,1,16,8]
print(sol.print_lis(arr))
