"""

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

https://takeuforward.org/data-structure/search-single-element-in-a-sorted-array/

"""

def single_element(nums):
    n=len(nums)
    if n==1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]

    low = 1
    high = n-2

    while low<=high:
        mid=(low+high)//2

        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        else:
            
            if (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]):
                #we are in left half and element is in right half
                #so we will discard the left half
                low = mid+1
            else:
                #we are in right half and element is in left half
                #we will discard the right half
                high = mid-1

print(single_element([1,1,2,3,3,4,4,8,8]))