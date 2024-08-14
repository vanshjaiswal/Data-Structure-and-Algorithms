"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12

"""



def canMakeBouquets(bloomDay, days: int, m, k) -> bool:
    bouquets = 0
    flowers = 0
    for bloom in bloomDay:
        if bloom <= days:
            flowers += 1
            if flowers == k:
                bouquets += 1
                flowers = 0
                if bouquets >= m:
                    return True
        else:
            flowers = 0
    return bouquets >= m

def minimum_bouquet(bloomDay, m, k):
    n=len(bloomDay)
    if n < m*k:
        return -1

    low = min(bloomDay)
    high = max(bloomDay)

    while low<=high:
        mid = (low + high)//2

        if canMakeBouquets(bloomDay, mid, m, k):
            high = mid-1
        else:
            low = mid + 1
    return low

# print(minimum_bouquet([7,7,7,7,12,7,7], 2, 3))
print(minimum_bouquet([1,10,3,10,2], 3, 1))


# def possible(nums, days, m, k):
#     count=0
#     bouquet=0
#     for i in range(len(nums)):
#         if nums[i]<=days:
#             count +=1
#         else:
#             bouquet = count//k
#             count = 0
#     bouquet = count//k 
#     if bouquet >= m:
#         return True
#     else:
#         return False