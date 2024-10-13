"""
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/

Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.

The solution will work for only positive values into the array 


"""

class Solution:
    def tabulation(self, nums, S):
        n=len(nums)
        dp = [[False for i in range(S+1)] for j in range(n)]

        #base case
        for i in range(n):
            dp[i][0] = True

        if nums[0] <= S:
            dp[0][nums[0]] =  True

        for i in range(1, n):
            for target in range(S+1):
                not_take = dp[i-1][target]
                take = False
                if nums[i] <= target:
                    take = dp[i-1][target- nums[i]]
                
                dp[i][target] =  take or not_take
        return dp


    def minimumDifference(self, nums) -> int:
        n= len(nums)
        S= sum(nums) 

        dp = self.tabulation(nums, S+1)

        mini =  float("inf")

        for i in range(S+1):
            if dp[n-1][i] == True: #that sum value is present
                S1  = i
                S2 = S - S1
                mini = min(mini, abs(S1 -  S2))

        return mini


sol = Solution()
nums = [3,9,7,3]
ans = sol.minimumDifference(nums)
print(ans)