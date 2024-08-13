"""
 Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. Now the array is rotated at some pivot point unknown to you. Find the index at which k is present and if k is not present return -1.

https://takeuforward.org/data-structure/search-element-in-a-rotated-sorted-array/

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4


"""

def rotated_array_search(nums, target):
    low, high = 0, len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[low] <= nums[mid]: #left part is sorted
            if nums[low] <= target and target <= nums[mid]:
                high = mid -1
            else:
                low = mid+1
        else: #right half is sorted
            if nums[mid]<=target and nums[high]>=target:
                low = mid + 1
            else:
                high = mid -1
        
    return -1

# print(rotated_array_search([4,5,6,7,0,1,2], 0))



"""

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

the array contains the duplicates,
return true if element exist or return False
"""

def rotated_array_search2(nums, target):
    low, high = 0, len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        elif nums[low] <= nums[mid]: #left part is sorted
            if nums[low] <= target and target <= nums[mid]:
                high = mid -1
            else:
                low = mid+1
        else: #right half is sorted
            if nums[mid]<=target and nums[high]>=target:
                low = mid + 1
            else:
                high = mid -1
        
    return False

print(rotated_array_search2([2,5,6,0,0,1,2], 3))