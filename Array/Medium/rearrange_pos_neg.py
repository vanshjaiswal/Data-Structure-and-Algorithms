"""

Problem Statement:

There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

Note: Start the array with positive elements.

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions. 

"""

def rarrange_pos_neg(nums):
    pos=0
    neg=1
    arr=[0]*len(nums)
    for i in range(len(nums)):
        if nums[i] >0 :
            arr[pos]=nums[i]
            pos +=2
        else:
            arr[neg]=nums[i]
            neg +=2
    return arr
print(rarrange_pos_neg([3,1,-2,-5,2,-4]))
