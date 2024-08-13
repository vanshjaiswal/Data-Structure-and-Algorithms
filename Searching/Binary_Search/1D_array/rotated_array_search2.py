"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.


Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

https://takeuforward.org/arrays/search-element-in-rotated-sorted-array-ii/
"""

def rotated_array_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return True
        elif nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
        
        elif nums[low] <= nums[mid]: #left half is sorted
            if nums[low] <= target and target <= nums[mid]:
                high = mid-1
            else:
                low = mid + 1
        elif nums[high] >= nums[mid]: #right half is sorted
            if nums[mid] <=  target and target <= nums[high]:
                low = mid + 1
            else:
                high = high -1
    return False

print(rotated_array_search([2,5,6,0,0,1,2], 3))
