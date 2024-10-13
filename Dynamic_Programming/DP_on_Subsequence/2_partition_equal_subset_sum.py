"""

https://leetcode.com/problems/partition-equal-subset-sum/description/


Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.


Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Solution:

This problem can be solved using subset sum=target problem,

if sum(arr) is odd return False as It can not divide into two parts

In even case S=sum(arr) so the subset sum will be S/2. If we can find the subset for whic
sum is equal to S/2 then other element of the array will give us that value of the S/2.

f(index, S/2)
"""

class Solution:
    def recursion(self, index, arr, target):
        if target ==0 :
            return True

        if index == 0:
            return arr[0]== target

        not_take = self.recursion(index-1, arr, target)
        take = False
        
        if arr[index]<=target:
            take = self.recursion(index-1, arr, target-arr[index])

        return take or not_take

    def recursion_driver(self, nums):
        n=len(nums)
        S= sum(nums)
        if S%2==0:
            output = self.recursion(n-1, nums, int(S/2))
            return output
        else:
            return False


    def memoization(self, index, arr, target, dp):

        if target ==0 :
            return True

        if index == 0:
            return arr[0]== target

        if dp[index][target] != -1:
            return dp[index][target]

        not_take = self.memoization(index-1, arr, target, dp)
        take = False
        
        if arr[index]<=target:
            take = self.memoization(index-1, arr, target-arr[index], dp)
        dp[index][target] = take or not_take
        return dp[index][target]

    def memoization_driver(self, nums):
        n=len(nums)
        S= sum(nums)
        target = int(S/2)
        dp = [[-1 for i in range(target+1)] for j in range(n)]
        
        if S%2==0:
            output = self.memoization(n-1, nums, target, dp)
            return output
        else:
            return False


    def tabulation(self, arr, k):
        n= len(arr)
        dp = [[False for i in range(k+1)] for j in range(n)]

        #handle the base case
        for i in range(n):
            dp[i][0] = True

        if arr[0]<=k:
            dp[0][arr[0]] = True

        for index in range(1, n):
            for target in range(k+1):
                not_take = dp[index-1][target]
                take = False
                
                if arr[index]<=target:
                    take = dp[index-1][target-arr[index]]
                dp[index][target] = take or not_take
            
        return dp[index][target]

    def tabulation_driver(self, nums):
        n=len(nums)
        S= sum(nums)
        target = int(S/2)
        
        if S%2==0:
            output = self.tabulation(nums, target)
            return output
        else:
            return False


    def space_optimization(self, arr, k):
        n=len(arr)
        prev = [False] * (k+1)
        prev[0] = True

        if arr[0] <= k :
            prev[arr[0]] = True

        for index in range(1, n): 
            cur = [False] * (k+1)
            cur[0] = True
            for target in range(k+1):

                not_take = prev[target]
                take = False
                
                if arr[index]<=target:
                    take = prev[target-arr[index]]
                cur[target] = take or not_take
            prev = cur

        return prev[target]

    def space_optimization_driver(self, nums):
        n=len(nums)
        S= sum(nums)
        target = int(S/2)
        
        if S%2==0 and n>1:
            output = self.space_optimization(nums, target)
            return output
        else:
            return False


sol = Solution()
nums = [1,5,11,5]
ans = sol.recursion_driver(nums)
print(ans)

ans = sol.memoization_driver(nums)
print(ans)
ans = sol.tabulation_driver(nums)
print(ans)

ans = sol.space_optimization_driver(nums)
print(ans)
