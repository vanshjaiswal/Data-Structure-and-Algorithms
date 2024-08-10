"""
 Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

A subarray is a contiguous non-empty sequence of elements within an array.
Example 1:
Input Format:
 N = 4, array[] = {3, 1, 2, 4}, k = 6
Result:
 2
Explanation:
 The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].
PRE_REQUISITE: longest_subarray_sumk.py
"""

def count_subarray(nums, k):
    prefixsum=0
    prefixdict={}
    count=0
    for i in range(len(nums)):
        prefixsum += nums[i]
        #check if the sum already exist then do not update it since we may have zero which can be the part of longest subarray but if we update the presum then index will be updated and we will not get the correct result 
        if prefixsum not in prefixdict.keys():
            prefixdict[prefixsum] = i
        if (prefixsum - k) in prefixdict.keys():
            count +=1
        if prefixsum ==k:
            count +=1
        

    return count

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) # size of the given array.
    mpp = {}
    preSum = 0
    cnt = 0

    mpp[0] = 1 # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt

def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    count = 0
    prefix_sum = 0
    prefix_sum_count = {0: 1}  # Initialize with prefix sum 0 and count 1
    
    for num in nums:
        prefix_sum += num  # Update the running prefix sum
        if (prefix_sum - k) in prefix_sum_count:
            count += prefix_sum_count[prefix_sum - k]  # Increment count if (prefix_sum - k) is found
        if prefix_sum in prefix_sum_count:
            prefix_sum_count[prefix_sum] += 1  # Update the frequency of the current prefix sum
        else:
            prefix_sum_count[prefix_sum] = 1  # Initialize the frequency if the prefix sum is seen for the first time
    
    return count


print(subarraySum([1], 0))
