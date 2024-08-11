"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

"""

#Using hashing

def majority_element(nums):
    n=len(nums)
    dic=dict(zip(set(nums), [0]*len(set(nums))))
    target_len = n//3
    ans=[]
    for i in nums:
        if dic[i]>=target_len:
            ans.append(i)
        else:
            dic[i]+=1
    return list(set(ans))

# print(majority_element([1,2,2,3,2]))

#Optimal Approach
"""
Boyer Moore's Voting Algorithm,
This is the most efficient way

"""

def majority_element_moore(nums):
    n=len(nums)
    count1, count2 = 0, 0
    element1, element2 = float("-inf"), float("-inf")

    for i in range(n):
        if count1==0 and element2 != nums[i]:
            count1 = 1
            element1 = nums[i]
        elif count2==0 and element1 != nums[i]:
            count2 = 1
            element2 = nums[i]
        elif element1 == nums[i]:
            count1 +=1
        elif element2 == nums[i]:
            count2 +=1    
        else:
            count1 -= 1
            count2 -= 1

    ls=[]
    cnt1=0
    cnt2=0
    for i in range(n):
        if nums[i]==element1:
            cnt1+=1  
        if nums[i]==element2:
            cnt2+=1
    
    thresold = n//3 + 1

    if cnt1 >= thresold:
        ls.append(element1)
    if cnt2 >= thresold:
        ls.append(element2)
    
    return ls

print(majority_element_moore([1,2,2,3,2]))