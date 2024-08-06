"""
https://leetcode.com/problems/max-consecutive-ones/description/
Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

"""

def consecutive(nums):
    prev_count=0
    count=0
    for i in range(len(nums)):
        if nums[i]==1:
            count +=1
        else:
            if count > prev_count:
                prev_count=count
            count=0
    if count > prev_count:
        prev_count=count
    return prev_count

