"""
Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero

Example 1:
Input Format
: N = 6, array[] = {9, -3, 3, -1, 6, -5}
Result
: 5
Explanation
: The following subarrays sum to zero:
{-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
Since we require the length of the longest subarray, our answer is 5
"""

#brute

def longest_subarray(nums):
    n=len(nums)
    longest = float("-inf")
    for i in range(n):
        s=0
        for j in range(i, n):
            s+=nums[j]
            if s==0:
                l=(j-i)+1
                longest = max(l, longest)
    return longest

# print(longest_subarray([9, -3, 3, -1, 6, -5]))
# print(longest_subarray([6, -2, 2, -8, 1, 7, 4, -10]))

#Optimal Kadane's algo

def longest_subarray_optimal(nums):
    prefix_dict = {}
    prefix_sum = 0
    longest = float("-inf")
    n=len(nums)
    for i in range(n):
        prefix_sum += nums[i]
        if prefix_sum == 0:
            l = i+1
        else:
            if prefix_sum not in prefix_dict.keys():
                prefix_dict[prefix_sum] = i
        
            else:
                l = i - prefix_dict[prefix_sum]
                
        longest = max(longest, l)
    return longest

print(longest_subarray([6, -2, 2, -8, 1, 7, 4, -10]))

