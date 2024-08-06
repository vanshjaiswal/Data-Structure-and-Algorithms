"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
"""

def single(nums):
    dic = dict(zip(set(nums), [0]*len(set(nums))))
    for i in nums:
        dic[i] += 1

    value_list=list(dic.values())
    key_list=list(dic.keys())
    
    
    mark = value_list.index(1)
  
    single_element = key_list[mark]
    return single_element

        
print(single([4,1,2,1,2]))
        
     