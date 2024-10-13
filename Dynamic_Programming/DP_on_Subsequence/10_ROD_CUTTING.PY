"""
https://www.geeksforgeeks.org/problems/rod-cutting0840/1

Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by 
cutting in two pieces of lengths 2 and 
6, i.e., 5+17=22.

"""

class Solution:
    def recursion(self, index, price, N):
        if index==0:
            return price[0] * N

        not_take = 0 + self.recursion(index-1, price,N)
        take = float("-inf")
        rod_length = index + 1
        if rod_length <= N:
            take = price[index]  + self.recursion(index, price, N-rod_length)

        return max(take, not_take)

    def tabulation(self,price, N):
        n=len(price)
        dp = [[0 for i in range(N+1)] for j in range(len(price))]

        #convert base case 
        for i in range(N+1):
            dp[0][i] = price[0] * i

        for index in range(1, n):
            for length in range(N+1):
                not_take = 0 + dp[index-1][length]
                take = float("-inf")
                rod_length = index + 1
                if rod_length <= length:
                    take = price[index]  + dp[index][length-rod_length]
                dp[index][length] = max(take, not_take)
        return dp[n-1][N]




sol=Solution()
N = 8
price=[1, 5, 8, 9, 10, 17, 17, 20]
ans=sol.recursion(N-1, price, N)
print(ans)

ans = sol.tabulation(price, N)
print(ans)
