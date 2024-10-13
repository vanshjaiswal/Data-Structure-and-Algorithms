class Solution:
    def fibonacci(self, n, dp):
        if n <= 1:
            return n

        #step 2 : check if the resulted is already calculated and stored in dp array
        if dp[n] != -1:     
            return dp[n]
        
        #step 3: If dp[n] does not exist already then we are calculating it first time
        # so we will calculate it and store the value at dp[n]
        dp[n] =  self.fibonacci(n-1, dp) + self.fibonacci(n-2, dp)

        return dp[n]
        



if __name__ == "__main__":
    sol = Solution()
    n=5
    dp = [-1] * (n+1)    #step 1: creating dp array
    ans = sol.fibonacci(n, dp)
    print(ans)