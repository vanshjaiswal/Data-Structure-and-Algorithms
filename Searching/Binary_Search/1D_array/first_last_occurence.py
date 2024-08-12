"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


lower bound = lower bound is giving the smallest index for which arr[index] >= target.

upper bound = upper bound is giving the smallest index for which arr[index] >  target

"""

def lower_bound(nums, target):
    low=0
    high = len(nums)-1
    ans= len(nums)

    while low<=high:
        mid = (low+high)//2

        if nums[mid] >=  target:
            ans=mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upper_bound(nums, target):
    low=0
    high = len(nums)-1
    ans= len(nums)

    while low<=high:
        mid = (low+high)//2

        if nums[mid] > target:
            ans=mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def first_last(nums, target):
    if nums==[]:
        return [-1,-1]
    n=len(nums)
    lower = lower_bound(nums, target)
    upper = upper_bound(nums, target) - 1
    # print(lower)
    if lower ==n:
        return [-1,-1]
    elif nums[lower] != target :
        return [-1,-1]
    else:
        return [lower, upper]


# print(first_last([5,7,7,8,8,10], 8))
# print(first_last([], 0))
print(first_last([2,2], 3))