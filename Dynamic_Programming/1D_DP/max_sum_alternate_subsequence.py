
"""
https://leetcode.com/problems/house-robber/description/

"""
class Solution:
    def rob(self, index, nums):
        if index == 0:
            return nums[0]
        if index < 0 :
            return 0


        pick =  nums[index] + self.rob(index-2, nums)

        non_pick = 0 + self.rob(index-1, nums)

        return max(pick, non_pick)

    #Time limit exceeded with recursion

    #Let's try DP

    def memoization(self, index, nums, dp):
        if index == 0:
            return nums[0]
        if index < 0:
            return 0

        if dp[index] != -1:
            return dp[index]

        pick = nums[index] + self.memoization(index-2, nums, dp)
        non_pick = 0 + self.memoization(index-1, nums, dp)

        dp[index] = max(pick, non_pick)
        return dp[index]

    def memoization_driver(self, nums):
        n=len(nums)
        dp = [-1] * (n+1)
        
        output = self.memoization(n-1, nums, dp)
        return output


    #tabulation
    def tabulation(self, nums):
        n=len(nums)
        dp = [-1] * (n+1)

        dp[0] = nums[0]
        #for the case of i-2 when i=1 we will get negative index, so we will not 
        #add the value of dp[i-2] to the pick and only take the current value
        #for i>0 we will add the value of dp[i-2]

        for i in range(1, n):
            pick = nums[i]
            if i>1:
                pick += dp[i-2]
            non_pick = 0 + dp[i-1]

            dp[i] = max(pick, non_pick)

        return dp[n-1]



    #Space Optimization

    def space_optimized(self, nums):
        prev = nums[0] #i-1
        prev2 = 0  #i-2
        n=len(nums)
        for i in range(1, n):
            pick = nums[i]
            if i>1:
                pick += prev2
            non_pick = 0 + prev
            cur_i = max(pick, non_pick)


            prev2=prev
            prev=cur_i

        return prev


sol = Solution()
nums = [2,7,9,3,1] #[1,2,3,1]

index = len(nums)-1
ans = sol.rob(index, nums)
print(ans)

ans = sol.memoization_driver(nums)
print(ans)

ans = sol.tabulation(nums)
print(ans)

ans = sol.space_optimized(nums)
print(ans)