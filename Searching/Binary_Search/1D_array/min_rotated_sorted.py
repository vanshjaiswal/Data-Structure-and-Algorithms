"""
Find the minimum element in the rotated sorted array.
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.


https://takeuforward.org/data-structure/minimum-in-rotated-sorted-array/
"""

#optimal 1
def minimum_rotated(nums):
    low=0
    high = len(nums)-1
    m=float("inf")
    while low<=high:
        mid = (low+high)//2

        if nums[low]<=nums[mid]: #left half is sorted
            m = min(m, nums[low])
            low = mid + 1 #discarding the left half
        else: #rigt half is sorted
            m = min(m, nums[mid])
            high = mid -1 #discarding the right half
    return m

# print(minimum_rotated([3,4,5,1,2]))


#optimal 2 Optimising the binary search

def minimum_sorted_optimal2(nums):
    low=0
    high=len(nums)-1
    m=float("inf")
    while low<=high:
        if nums[low]<=nums[high]:
            m=min(m, nums[low])
            return m
        mid=(low+high)//2
        
        if nums[low] <= nums[mid]: #left half is sorted
            m = min(m , nums[low])
            low = mid+1 #discard the left half
        else: #right half is sorted
            m= min(m, nums[mid])
            high = mid - 1 #discard the right half
        
    return m
print(minimum_sorted_optimal2([3,4,5,1,2]))