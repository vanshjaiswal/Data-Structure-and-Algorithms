"""
https://leetcode.com/problems/shortest-common-supersequence/description/

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.


"""
class Solution:
    def tabulation(self, text1, text2):
        m=len(text1)
        n=len(text2)
        dp = [[-1 for j in range(n+1)] for i in range(m+1)]
        #base case: shift the index value by 1 to the right. so that we can conisder the -1 index ind<0 as 0
        # if ind1 < 0 or ind2 < 0:
        #     return 0
        """
        The above base case can be modified as
        if ind1 == 0 or ind2 == 0:
            return 0

        -1, 0, 1, 2, 3..... n-1
        0, 1, 2, 3, 4 .......n-1, n

        """
        for i in range(m+1):
            dp[i][0] = 0
        
        for j in range(n+1):
            dp[0][j] = 0

        #copy the recursion
        for ind1 in range(1, m+1):
            for ind2 in range(1, n+1):
                #match
                if text1[ind1-1] == text2[ind2-1]:
                    #here 1 signifies that we found 1 macthing character
                    dp[ind1][ind2] =  1 + dp[ind1-1][ind2-1]
                #not match case
                else:
                    dp[ind1][ind2] = max(dp[ind1][ind2-1], dp[ind1-1][ind2])
        return dp

    def supersequence(self, str1, str2):
        dp = self.tabulation(str1, str2)

        i=len(str1)
        j=len(str2)
        ans= ""
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                ans += str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]  > dp[i][j-1]:
                ans += str1[i-1]
                i-=1
            else:
                ans +=str2[j-1]
                j-=1
        
        while i > 0:
            ans += str1[i-1]
            i-=1
        while j>0:
            ans += str2[j-1]
            j-=1

        return ans[::-1]

sol = Solution()
str1 = "brute"
str2 = "groot"

ans = sol.supersequence(str1, str2)
print(ans)
