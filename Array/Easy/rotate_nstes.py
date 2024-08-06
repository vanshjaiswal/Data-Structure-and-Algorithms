"""
https://leetcode.com/problems/rotate-array/solutions/5550096/video-using-remainder-with-3-solutions/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""

def rotate(nums,k):
    k=k%len(nums)  #if k > len(nums then after len(nums) time we will get the same array. so if k is greater then use the remainder)
    for i in range(k):
        last=nums.pop()
        nums.insert(0,last)
    return nums

print(rotate([1,2,3,4,5,6,7], 3))

def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    rotated = [0] * n

    for i in range(n):
        rotated[(i + k) % n] = nums[i]
    
    for i in range(n):
        nums[i] = rotated[i]