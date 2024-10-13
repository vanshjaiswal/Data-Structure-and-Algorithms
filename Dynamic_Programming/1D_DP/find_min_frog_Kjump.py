class Solution:
    def recursion(self, index, H, k):
        if index == 0:
            return 0

        min_step = float("inf")

        for j in range(1, k+1):
            if index-j >= 0:
                jump = self.recursion(index-j, H, k) + abs(H[index] - H[index-j])
                min_step = min(min_step, jump)

        return min_step

    def memoization(self, index, H, k, dp):
        if index == 0:
            return 0

        if dp[index] != -1:
            return dp[index]
        min_step = float("inf")
        for j in range(1, k+1):
            if index - j >=0 :
                jump = self.memoization(index-j, H,k,dp) + abs(H[index] - H[index-j])
                min_step = min(min_step, jump)

        dp[index] = min_step
        return dp[index]

    def memoization_driver(self, H, k):
        n = len(H)-1
        dp = [-1] * (n+1)
        output = self.memoization(n, H, k, dp)
        return output


    def tabulation(self, H, k):
        n=len(H)
        dp = [-1] * (n + 1) 
        dp[0] = 0

        for i in range(1, n):
            min_step = float("inf")
            for j in range(1, k+1):
                if i-j >= 0: #index - j
                    jump = dp[i-j] + abs(H[i] - H[i-j])
                    min_step = min(min_step, jump)

            dp[i] = min_step
        return dp[n-1]
    #here there is no need of space  optimization because we need k values to be stored for 
    # getting the previous value, at every point we are having k steps so we need these values
    #to be stored in the list and we have to carry that list. so in worst case when k=n we
    #will still get space complexity of O(n)
if __name__ == "__main__":
    sol = Solution()
    H =  [10, 30, 40, 50, 20]
    n=len(H)
    k=3
    ans = sol.recursion(n-1, H, k)
    print("Recursion: ", ans)

    ans = sol.memoization_driver(H, k)
    print("Memoization: ", ans)

    ans = sol.tabulation(H, k)
    print("Tabulation: ", ans)

    # ans = sol.space_optimized_frog(H, n)
    # print("space_optimized: ", ans)