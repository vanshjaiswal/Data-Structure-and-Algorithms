"""
Problem Statement: You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
The floor of x is the largest element in the array which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x.

Example 1:
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.

"""

def floor_ceiling(nums, target):
    low, high, ans = 0 , len(nums)-1, len(nums)
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return (nums[mid], nums[mid])
        elif nums[mid] < target :
            low = mid +1
        else:
            high = mid -1
    return ( nums[high], nums[low])

# print(floor_ceiling([3, 4, 4, 7, 8, 10], 5))
print(floor_ceiling([3, 4, 4, 7, 8, 10], 8))