"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""

# def sort_colors(nums):
    
#     zero=nums.count(0)
#     one=nums.count(1)
#     two=nums.count(2)
#     zero_list=[0]*zero
#     one_list=[1]*one
#     two_list=[2]*two
#     arr=zero_list + one_list + two_list
#     for i in range(len(nums)):
#         nums[i]=arr[i]
#     return nums

# print(sort_colors([2,0,2,1,1,0]))

#better

def sort_colors(nums):
    zero=0
    one=0
    two=0
    for i in range(len(nums)):
        if nums[i]==0:
            zero +=1
        elif nums[i]==1:
            one += 1
        else:
            two+=1
    arr = ([0]*zero) + ([1]*one) + ([2]*two)
    print(arr)
    for i in range(len(arr)):
        nums[i]=arr[i]
    return nums
# print(sort_colors([2,0,2,1,1,0]))

#Optimal approach

"""
Three pointer approach. 

https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/

Dutch National flag algorithm. 

This algorithm contains 3 pointers i.e. low, mid, and high, and 3 main rules.  The rules are the following:

arr[0….low-1] contains 0. [Extreme left part]
arr[low….mid-1] contains 1.
arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array

Approach:

Note: Here in this tutorial we will work based on the value of the mid pointer.

The steps will be the following:

First, we will run a loop that will continue until mid <= high.
There can be three different values of mid pointer i.e. arr[mid]
If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.
In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.
"""

def dutch_algorithm_sorting(nums):
    left = 0
    mid = 0
    high = len(nums)-1

    while mid <= high:
        if nums[mid]==0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid]==1:
            mid +=1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

print(dutch_algorithm_sorting([1,2,0]))

def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr
# print(sortArray([1,2,0]))