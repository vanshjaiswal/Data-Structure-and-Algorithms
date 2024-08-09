"""
Kadane's Algorithm : Maximum Subarray Sum in an Array

Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Example 1:
Input:
arr = [-2,1,-3,4,-1,2,1,-5,4] 

Output: 6

Explanation:
 [4,-1,2,1] has the largest sum = 6. 

"""

#brute force
def largest_sum(nums):
    m=float("-inf")
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            s=0
            for k in range(i,j+1):
                s+=nums[k]

            m = max(m, s)
    return m

print(largest_sum([-2,1,-3,4,-1,2,1,-5,4] ))

# better
def largest_sum(nums):
    m=float("-inf")
    for i in range(len(nums)):
        s=0
        for j in range(i, len(nums)):
            s+=nums[j]

            m = max(m, s)
    return m

print(largest_sum([-2,1,-3,4,-1,2,1,-5,4] ))

#optimised
def largest_sum(arr):
    maxi = float("-inf") # maximum sum
    sum = 0
    n=len(arr)
    for i in range(n):
        sum += arr[i]

        if sum > maxi:
            maxi = sum

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0

    # To consider the sum of the empty subarray
    # uncomment the following check:

    #if maxi < 0: maxi = 0

    return maxi
print(largest_sum([-2,1,-3,4,-4,2,1,-5,4] ))


