"""
https://leetcode.com/problems/longest-common-subsequence/description/

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3


"""

class Solution:

    def recursion(self, ind1, ind2, S1, S2):
        if ind1 < 0 or ind2 < 0:
            return 0

        #match
        if S1[ind1] == S2[ind2]:
            #here 1 signifies that we found 1 macthing character
            return 1 + self.recursion(ind1-1, ind2-1, S1, S2) 

        #not match case
        else:
            #0 means matching characters are not found so we are changing the 
            # ind1 and fixing ind2 in one case and vice-versa in another then we are
            # taking the max of both cases. since we have to return the maximum/longest
            #matching subsequence
            return 0 + max(self.recursion(ind1, ind2-1, S1, S2), self.recursion(ind1-1, ind2, S1, S2) )

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
        return dp[m][n]

    def space_optimized(self, s1, s2):
        n = len(s1)
        m = len(s2)

        # Initialize two arrays, 'prev' and 'cur', to store the DP values
        prev = [0] * (m + 1)
        cur = [0] * (m + 1)

        # Loop through the characters of both strings to compute LCS
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    # If the characters match, increment LCS length by 1
                    cur[ind2] = 1 + prev[ind2 - 1]
                else:
                    # If the characters do not match, take the maximum of LCS
                    # by excluding one character from s1 or s2
                    cur[ind2] = max(prev[ind2], cur[ind2 - 1])
            
            # Update 'prev' to be the same as 'cur' for the next iteration
            prev = cur[:]

        # The value in 'prev[m]' represents the length of the Longest Common Subsequence
        return prev[m]
sol = Solution()
text1 = "abcde"
text2 = "ace"

text1 = "ABCDGH"
text2 = "ACDGHR"

text1 = "mbadm"
text2 = text1[::-1]


# ans =  sol.recursion(len(text1)-1, len(text2)-1, text1, text2)
# print(ans)

ans =  sol.tabulation(text1, text2)
print(ans)

ans =  sol.space_optimized(text1, text2)
print(len(text1)-ans )