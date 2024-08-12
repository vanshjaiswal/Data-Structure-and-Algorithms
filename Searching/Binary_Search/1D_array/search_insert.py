"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


"""

def search_insert(nums, target):
    low=0
    high=len(nums)-1
    
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low = mid + 1
        else:
            high = mid-1
    return low

print(search_insert([1,3,5,6],5))

def search_insert_best(nums, target):
    low=0
    high=len(nums)-1
    ans = len(nums)
    
    while low<=high:
        mid=(low+high)//2

        if nums[mid] >= target:
            ans = mid
            high = high -1
        else:
            low = mid +1
    return ans

print(search_insert_best([1,3,5,6],5))