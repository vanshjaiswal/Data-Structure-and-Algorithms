"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

nums[a] + nums[b] + nums[c] + nums[d] == target

a, b, c, and d are distinct.

nums[a] + nums[b] + nums[c] + nums[d] == target

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


"""

#Brute Force

def fourSum(nums, target):
    st=set()
    n=len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        temp = [nums[i] , nums[j] , nums[k] , nums[l]]
                        temp=sorted(temp)
                        st.add(tuple(temp))

    result = [list(x) for x in st]
    return result

# print(fourSum([1,0,-1,0,-2,2], 0))
# print(fourSum([2,2,2,2,2], 8))


#Better Solution:
"""
In this approach we will use the hashset/dic for removing the fourth loop
and will try to find the number based on below criteria

nums[i] + nums[j] + nums[k] + nums[l] = target

nums[l] = target - (nums[i] + nums[j] + nums[k])

"""

def fourSum_better(nums, target):
    st=set()
    # dic={}
    n=len(nums)
    for i in range(n):
        for j in range(i+1, n):
            dic={}
            for k in range(j+1, n):
                req = target - (nums[i] + nums[j] + nums[k])
                if req in dic.keys():
                    temp = [nums[i] , nums[j] , nums[k], nums[dic[req]]]
                    temp=sorted(temp)
                    st.add(tuple(temp))
                else:
                    dic[nums[k]] = k

    result = [list(x) for x in st]
    return result

# print(fourSum_better([1,0,-1,0,-2,2], 0))
# print(fourSum_better([2,2,2,2,2], 8))

# [1,0,-1,0,-2,2]
[-2,-1,0,0,1,2]

#Optimal Approach using three pointer

def fourSum_optimal(nums, target):
    n=len(nums)
    nums=sorted(nums)
    ans=[]
    for i in range(n):
        
        if i != 0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1, n):
            if j > i+1 and nums[j]==nums[j-1]:
                continue

            k=j+1
            l=n-1
            
            while k<l:
                thresold = nums[i] + nums[j] + nums[k] + nums[l]

                if thresold > target:
                    l-=1
                elif thresold < target:
                    k+=1
                else:
                    temp = [nums[i] , nums[j] , nums[k] , nums[l]]
                    ans.append(temp)
                    k+=1
                    l-=1

                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1
                    
          
    
    return ans

print(fourSum_optimal([1,0,-1,0,-2,2], 0))
# print(fourSum_optimal([2,2,2,2,2], 8))

                
