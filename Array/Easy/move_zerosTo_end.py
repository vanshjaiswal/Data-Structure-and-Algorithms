"""
Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

Example 1:
Input:
 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output:
 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation:
 All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

Example 2:
Input:
 1,2,0,1,0,4,0
Output:
 1,2,1,4,0,0,0

"""

def zeros_end(nums):
    zeros=[]
    non_zeros=[]
    for i in nums:
        if i==0:
            zeros.append(i)
        else:
            non_zeros.append(i)
    print(non_zeros, zeros)
    # non_zeros
    non_zeros=non_zeros + zeros   
    print(non_zeros)

    for i in range(len(non_zeros)):
        nums[i]= non_zeros[i]   
    return nums

print(zeros_end([0,1,0,3,12]))  
        
