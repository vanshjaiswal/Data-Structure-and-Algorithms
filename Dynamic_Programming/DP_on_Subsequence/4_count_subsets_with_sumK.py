class Solution:
    def tabulation(self, arr, k):
        n= len(arr)

        dp =  [[0 for i in range(k+1)]for j in range(n)]

        for i in range(n): #base case 1
            dp[i][0] = 1

        if arr[0]<=k:
            dp[0][arr[0]] = 1

        for index in range(1, n):
            for target in range(k+1):
                not_take = dp[index-1][target]
                take= 0
                if arr[index]<= target:
                    take = dp[index-1][target - arr[index]]
                
                dp[index][target] = take + not_take

        return dp[n-1][k]

    def count_sum_k(self, arr, k):
        dp = self.tabulation(arr, k)
        print(dp)
        n=len(arr)
        count= 0
        for i in range(1, n):
            if dp[i][k]== True:
                count +=1

        return count


sol = Solution()

# arr = [5, 2, 3, 10, 6, 8] 
# k = 10

arr2 = [2, 5, 1, 4, 3]
k2 = 10
# ans = sol.count_sum_k(arr, k)
ans2 = sol.tabulation(arr2, k2)
# print(ans)
print(ans2)

# [[True, False, True, False, False, False, False, False, False, False, False], 
# [True, False, True, False, False, True, False, True, False, False, False], 
# [True, True, True, True, False, True, True, True, True, False, False], 
# [True, True, True, True, True, True, True, True, True, True, True], 
# [True, True, True, True, True, True, True, True, True, True, True]]




# 0: [[True, False, False, False, False, True, False, False, False, False, False], 
# 1: [True, False, True, False, False, True, False, True, False, False, False], 
# 2: [True, False, True, True, False, True, False, True, True, False, True], 
# 3: [True, False, True, True, False, True, False, True, True, False, True], 
# 4: [True, False, True, True, False, True, True, True, True, True, True], 
# 5: [True, False, True, True, False, True, True, True, True, True, True]]