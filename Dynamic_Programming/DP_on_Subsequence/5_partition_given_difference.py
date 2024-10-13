class Solution:

    def memoization(self, index, arr, target, dp):
        #updated base case 
        if index==0:
            if target==0 and arr[0]==0:
                return 2
            if target == 0 or arr[0] == target:
                return 1
            return 0
        # print(index)
        if dp[index][target] != -1:
            return dp[index][target]

        not_take = self.memoization(index-1, arr, target, dp)
        take=0
        if arr[index]<=target:
            take=self.memoization(index-1, arr, target-arr[index], dp)

        dp[index][target] = take + not_take

        return dp[index][target]

    def memoization_driver(self, arr, d):
        n= len(arr)
        total_sum = sum(arr)
        s2 = (total_sum-d)//2
        dp = [[-1 for i in range(s2+1)] for j in range(n)]
        index = n-1
        output = self.memoization(index, arr, s2, dp)
        return output




    def tabulation(self, arr, k):
        #updated base cases 
        n= len(arr)
        dp = [[False for i in range(k+1)] for j in range(n)]

        for i in range(n):
            dp[i][0] = True

        if arr[0]<=k:
            dp[0][arr[0]] = True


        for index in range(1, n):
            for target in range(k+1):
                not_take  = dp[index-1][target]
                take = False
                if arr[index] <= target:
                    take = dp[index-1][target -  arr[index]]

                dp[index][target] = take or not_take

        return dp


    def partition_given_difference(self, nums, d):
        s=sum(nums)
        n=len(nums)
        dp = self.tabulation(nums, s)
        # print(dp)
        count = 0
        for i in range((s+1)):
            if dp[n-1][i] == True:
                S1 = i
                S2 = s-S1
                # print(S1, S2)
                if abs(S1 - S2) == d:
                    count += 1

        return count

sol = Solution()

arr = [1, 3, 3, 2, 1]
d = 5
ans = sol.partition_given_difference(arr, d)
print(ans)

# s2 = (sum(arr) - d)//2
# print(s2)
# ans = sol.memoization_driver(arr, d)
# print(ans)

