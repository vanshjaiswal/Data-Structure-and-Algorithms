"""
Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum. 

Input: n = 6, arr[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
Explanation: Here there exists a subset with sum = 9, 4+3+2 = 9.


"""

class Solution:
    def recursion(self, index, arr, target):
        if target==0:
            return True

        if index==0:
            return arr[index]==target

        #not_Take
        not_take = self.recursion(index-1, arr, target)

        take=False
        if target >= arr[index]:
            take = self.recursion(index-1, arr, target-arr[index])

        return take or not_take




    def memoization(self, index, arr, target, dp):
        if target==0:
            return True
        if index==0:
            return arr[index]==target

        if dp[index][target] != -1:
            return dp[index][target]

        #not_Take
        not_take = self.memoization(index-1, arr, target, dp)

        take=False
        if target >= arr[index]:
            take = self.memoization(index-1, arr, target-arr[index], dp)
        dp[index][target] = take or not_take

        return dp[index][target]

    def memoization_driver(self, arr, k):
        n=len(arr)

        dp=[[-1 for i in range(k+1)] for j in range(n)]
        output = self.memoization(n-1, arr, k, dp)
        return output

    def tabulation(self, arr, k):
        n=len(arr)
        #Declare a dp of size [N][K+1]
        dp = [[False for i in range(k+1)] for j in range(n)]

        #Convert the base case of the recursion into the dp array
        #1: if target==0: return True, so we can assign the first column target=0 as True

        for i in range(n):
            dp[i][0]=True

        #2nd Base case: if index==0: return arr[0]==target
        # for the first row of the dp array we will set dp[0][arr[0]] = True
        #whatever the value of the first element of the arr we can set that value to True in the dp array's first row.
        #We will only asssign this value when arr[0] <= target
        if arr[0] <= k:
            dp[0][arr[0]]=True

        #Write the nested for loops, number of for loops is equal to the number of changing parameters in the recursion.

        for index in range(1, n): #since 0 is already considered
            for target in range(k+1): #for every index we have target from 0 to K
                #copy paste the recursion
                #not_Take
                # not_take = self.recursion(index-1, arr, target)
                not_take = dp[index-1][target]

                take=False
                if target >= arr[index]:
                    # take = self.recursion(index-1, arr, target-arr[index])
                    take = dp[index-1][target-arr[index]]

                dp[index][target] = take or not_take
        
        return dp[index][target]



    def space_optimization(self, arr, k):
        n=len(arr)
        #Create a array prev and set 0th index as True and arr[0]th index as True
        
        prev = [False] * (k+1)
        prev[0] = True
        if arr[0] <= k:
            prev[arr[0]] = True
        




        #Write the nested for loops, number of for loops is equal to the number of changing parameters in the recursion.

        for index in range(1, n): #since 0 is already considered
            cur = [False] * (k+1)
            cur[0] = True
            for target in range(k+1): #for every index we have target from 0 to K
                #copy paste the recursion
                #not_Take
                # not_take = self.recursion(index-1, arr, target)
                not_take = prev[target]

                take=False
                if target >= arr[index]:
                    # take = self.recursion(index-1, arr, target-arr[index])
                    take = prev[target- arr[index]]

                cur[target] = take or not_take
            prev = cur
        
        return prev[target]

        
        

sol =Solution()
arr = [3, 34, 4, 12, 5, 2]
k=30
n=len(arr)
ans = sol.recursion(n-1, arr, k)
print(ans)

ans = sol.memoization_driver(arr, k)
print(ans)

ans = sol.tabulation(arr, k)
print(ans)

ans = sol.space_optimization(arr, k)
print(ans)
        
