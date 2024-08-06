"""

https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array/


Problem Statement: Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.

2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.


Example 1:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

"""
#return pair
def twoSum(nums, k):
    dic={}
    for i in nums:
        dic[i]=k-i
        if (k-i) in dic.keys():
            return [i,k-i]
    return [-1,-1]

# print(twoSum([2,6,5,8,11], 14))

def twoSum(nums, k):
    dic={}
    for i in range(len(nums)):
        if (k-nums[i]) in dic.keys():
            return [i,nums.index(k-nums[i])]
        dic[nums[i]]=k-nums[i]
        
    return [-1,-1]
# print(twoSum([7,6,7,8,11], 14))


#optimal withouth hashmap, two pointer approach

def twoSum(nums, k):
    nums1=sorted(nums)
    left=0
    right=len(nums)-1

    for i in range(len(nums)):
        s = nums[left] + nums[right]
        if s == k:
            return [nums.index(nums[left]), nums.index(nums[right])]
        elif s<k:
            left += 1
        elif s>k:
            right -= 1
    else:
        return [-1,-1]
print(twoSum([7,6,7,8,11], 14))
        
        