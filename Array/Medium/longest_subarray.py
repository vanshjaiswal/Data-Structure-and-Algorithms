"""
 You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.

 Example 1:
Input:
 [100, 200, 1, 3, 2, 4]

Output:
 4

"""

#brute force

def longest_subarray(nums):
    max_array = 0
    
    for i in range(len(nums)):
        x=nums[i]
        iter = 0
        count = 1
        while iter < len(nums):
            # print(x)
            if x+1 in nums:
                x +=1
                count += 1
            else:
                break
            iter +=1
        if count > max_array:
            max_array=count
    return max_array

# print(longest_subarray([3, 8, 5, 7, 6]))




#Better approach
"""
In this approach we are going to use the sorting.

Algorithm:
We will consider 3 variables, 
‘lastSmaller’ →(to store the last included element of the current sequence), 
‘cnt’ → (to store the length of the current sequence), 
‘longest’ → (to store the maximum length).
Initialize ‘lastSmaller’ with ‘INT_MIN’, ‘cnt’ with 0, and ‘longest’ with 1(as the minimum length of the sequence is 1).
The steps are as follows:

First, we will sort the entire array.
To begin, we will utilize a loop(say i) to iterate through each element one by one.
For every element, we will check if this can be a part of the current sequence like the following:
If arr[i]-1 == lastSmaller: The last element in our sequence is labeled as 'lastSmaller' and the current element 'arr[i]' is exactly 'lastSmaller'+1. It indicates that 'arr[i]' is the next consecutive element. To incorporate it into the sequence, we update 'lastSmaller' with the value of 'arr[i]' and increment the length of the current sequence, denoted as 'cnt', by 1.
If arr[i] == lastSmaller: If the current element, arr[i], matches the last element of the sequence (represented by 'lastSmaller'), we can skip it since we have already included it before.
Otherwise, if lastSmaller != arr[i]: On satisfying this condition, we can conclude that the current element, arr[i] > lastSmaller+1. It indicates that arr[i] cannot be a part of the current sequence. So, we will start a new sequence from arr[i] by updating ‘lastSmaller’ with the value of arr[i]. And we will set the length of the current sequence(cnt) to 1.
Every time, inside the loop, we will compare ‘cnt’ and ‘longest’ and update ‘longest’ with the maximum value. longest = max(longest, cnt)
Finally, once the iteration is complete, we will have the answer stored in the variable ‘longest’.


"""
def longest_subarray2(nums):
    lastSmaller=float("-inf")
    count = 1
    longest = 1
    nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i]-1==lastSmaller:
            lastSmaller  = nums[i]
            count +=1
        elif nums[i] != lastSmaller:
            lastSmaller = nums[i]
            count = 1
        longest = max(longest, count)
    return longest

# print(longest_subarray2([3, 8, 5, 7, 6]))


#Optimal
"""
https://takeuforward.org/data-structure/longest-consecutive-sequence-in-an-array/

"""

def longest_subarray3(nums):
    n=len(nums)
    largest=0
    if n==0:
        return 0
    
    arr = set(nums)

    for i in arr:
        if i-1 not in arr:
            x=i
            count=1
            while x+1 in arr:
                x+=1
                count+=1
            largest = max(largest, count)
    return largest

print(longest_subarray3([3, 8, 5, 7, 6]))

