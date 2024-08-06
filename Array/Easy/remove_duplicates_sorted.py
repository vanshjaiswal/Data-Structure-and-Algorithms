"""
https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/

Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.

Example 1:
Input:
 arr[1,1,2,2,2,3,3]

Output:
 arr[1,2,3,_,_,_,_]

Explanation:
 Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

"""

def duplicates_element(nums):
    n=len(nums)
    arr = ["_"]*n
    s=sorted(list(set(nums)))
    k=len(s)

    for i in range(len(s)):
        arr[i]=s[i]
    return k, arr


# print(duplicates_element([1,1,2]))
"""
nums = [1,1,2,2,2,3,3]
nums = [1,2,2,2,2,3,3] i=1, j=2
nums = [1,2,3,2,2,3,3] i=2, j=5
"""
def removeDuplicates(nums):
    i=1
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i=i+1
            nums[i] = nums[j]
    return i #unique values








