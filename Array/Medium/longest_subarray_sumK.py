"""
Given an array arr containing n integers and an integer k. Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

NOTE: subarray contains the consecutive elemenets only 

Input :
arr[] = {10, 5, 2, 7, 1, 9}, k = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}.
"""

#Brute_Force:
#Find the sum of all sub array and then find the sum==k for largest value.

def largest_subarray(nums,k):
    n = len(nums) # size of the array.

    length = 0
    for i in range(n): # starting index
        for j in range(i, n): # ending index
            # add all the elements of
            # subarray = a[i...j]:
            s = 0
            for K in range(i, j+1):
                s += nums[K]

            if s == k:
                length = max(length, j - i + 1)
    return length

# print(largest_subarray([10, 5, 2, 7, 1, 9], 15))



#from n3 to n2


def largest_subarray(nums,k):
    n = len(nums) # size of the array.

    length = 0
    for i in range(n): # starting index
        s=0
        for j in range(i, n): # ending index
            # add all the elements of
            # subarray = a[i...j]:
            s+=nums[j]

            if s == k:
                length = max(length, j - i + 1)
    return length
# print(largest_subarray([10, 5, 2, 7, 1, 9], 15))



#Better solution
""" 
Using Hashing:

https://takeuforward.org/data-structure/longest-subarray-with-given-sum-k/

"""

def largest_subarray(nums, k):
    prefix_dict = {}
    prefix_sum = 0
    largest = 0

    for i in range(len(nums)):
        #check if the sum already exist then do not update it since we may zero which can be the part of longest subarray but if we update the presum then index will be updated and we will not get the correct result 
        
        prefix_sum += nums[i]
        if prefix_sum not in prefix_dict.keys():
            prefix_dict[prefix_sum]=i

        if prefix_sum == k :
            largest = i+1
        if ((prefix_sum-k) in prefix_dict.keys()):
            print("Inside", prefix_dict)
            largest = max(largest, abs(i - prefix_dict[prefix_sum-k]))
            print("Largest", largest)
    print(prefix_dict)
    return largest
# print(largest_subarray([3,4,2,3,1,2], 3))    
# print(largest_subarray([2,0,0,0,0,0,3], 3))   


#optimal approach

def longest_subarray(nums,k):
    n = len(a) # size of the array.

    left, right = 0, 0 # 2 pointers
    Sum = a[0]
    maxLen = 0
    while right < n:
        # if sum > k, reduce the subarray from left
        # until sum becomes less or equal to k:
        while left <= right and Sum > k:
            Sum -= a[left]
            left += 1

        # if sum = k, update the maxLen i.e. answer:
        if Sum == k:
            maxLen = max(maxLen, right - left + 1)

        # Move forward the right pointer:
        right += 1
        if right < n: Sum += a[right]

    return maxLen
print(largest_subarray([3,4,2,3,1,2], 3))  