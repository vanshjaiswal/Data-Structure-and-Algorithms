"""
https://leetcode.com/problems/target-sum/

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

"""

class Solution:
    def recursion(self, index, arr, exp, target):
        if index == 0:
            if arr[0]==0 and exp == target:
                return 2
            elif exp + arr[0] == target or exp - arr[0] == target:
                return 1
            
            return 0

        neg = 0
        pos = self.recursion(index-1, arr, exp + arr[index], target)
        neg = self.recursion(index-1, arr, exp-arr[index], target)

        return pos + neg
            
    def findTargetSumWays(self, nums, target):
        n=len(nums)
        return self.recursion(n-1, nums, 0, target)

    def memoization(self, index, arr, exp, target, dp):
        if index == 0:
            if arr[0]==0 and exp == target:
                return 2
            elif exp + arr[0] == target or exp - arr[0] == target:
                return 1
            
            return 0

        if dp[index][exp] != -1:
            return dp[index][exp]

        neg = 0
        pos = self.memoization(index-1, arr, exp + arr[index], target, dp)
        neg = self.memoization(index-1, arr, exp - arr[index], target, dp)
        dp[index][exp] = pos + neg
        print(dp)
        return dp[index][exp]

    def memoization_driver(self, nums, target):
        n=len(nums)
        s=sum(nums)
        dp=[[-1 for i in range(s+1)] for j in range(n)]
        return self.memoization(n-1, nums, 0, target, dp)

    def tabulation(self, arr, k):
        #updated base cases 
        n= len(arr)

        dp = [[0 for i in range(k+1)] for j in range(n)]
        if nums[0] == 0:
            dp[0][0] = 2 # 2 cases - pick and not pick
        else:
            dp[0][0] = 1 # 1 case - not pick
        
        if nums[0] != 0 and nums[0] <= k:
            dp[0][nums[0]] = 1

        # for i in range(n):
        #     dp[i][0] = 1

        # if arr[0]<=k:
        #     dp[0][arr[0]] = 1


        for index in range(1, n):
            for target in range(k+1):
                not_take  = dp[index-1][target]
                take = 0
                if arr[index] <= target:
                    take = dp[index-1][target -  arr[index]]

                dp[index][target] = take + not_take

        return dp[index][target]

    def findTargetSumWays(self, nums, target):
        n=len(nums)
        s=sum(nums)
        if s < target :
            return 0
        if (s-target) % 2 != 0:
            return 0
        s2= (s - target)//2
        return self.tabulation(nums, s2)

    # def partition_given_difference(self, nums, d):
    #     s=sum(nums)
    #     n=len(nums)
    #     dp = self.tabulation(nums, s)
    #     # print(dp)
    #     count = 0
    #     for i in range((s+1)):
    #         if dp[n-1][i] == True:
    #             S1 = i
    #             S2 = s-S1
    #             # print(S1, S2)
    #             if abs(S1 - S2) == d:
    #                 count += 1

    #     return count

sol = Solution()
nums = [1,1,1,1,1]
target = 3
# s2= (sum(nums) - target)//2
# ans= sol.findTargetSumWays(nums, target)
# print(ans)

# ans= sol.memoization_driver(nums, target)
# print(ans)

ans= sol.findTargetSumWays(nums, target)
print(ans)
