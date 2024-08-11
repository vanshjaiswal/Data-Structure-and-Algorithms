"""
Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/
"""

#Brute Force
def threeSum(nums):
    n=len(nums)
    st=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] == 0:
                    temp = [nums[i] , nums[j] , nums[k]]
                    temp=sorted(temp)
                    st.add(tuple(temp))
    st=list(st)
    result = [list(i) for i in st]
    return result

# print(threeSum([-1,0,1,2,-1,-4]))


#better

def threeSum_better(nums):
    st=set()
    n=len(nums)
    for i in range(n):
        dic={}
        for j in range(i+1, n):
            k=-(nums[i]+nums[j])
            if k in dic.keys():
                temp=[nums[i], nums[j], nums[dic[k]]]
                temp=sorted(temp)
                st.add(tuple(temp))
            else:
                dic[nums[j]]=j
    
    result = [list(x) for x in st]
    return result

# print(threeSum_better([0,0,0]))


#Optimal

"""
using Two pointers

https://takeuforward.org/data-structure/3-sum-find-triplets-that-add-up-to-a-zero/

"""

def threeSum_Optimal(nums):
    nums=sorted(nums)
    n=len(nums)
    ans=[]

    for i in range(n):
        if i!=0 and nums[i]==nums[i-1]:
            continue
        
        j = i+1
        k = n-1
        while j <k:
            s= nums[i] + nums[j] + nums[k]
            if s<0:
                j+=1
            elif s>0:
                k-=1
            else:
                ans.append([nums[i] , nums[j] , nums[k]])
                j+=1
                k-=1

                #skip the duplicates and increment the value of j and k for skipping
                while j < k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k] == nums[k+1]:
                    k-=1
    return ans
            
print(threeSum_Optimal([-1,0,1,2,-1,-4]))   

        