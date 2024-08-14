"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


https://takeuforward.org/binary-search/koko-eating-bananas/

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Input: piles = [30,11,23,4,20], h = 5
Output: 30
"""
import math


def calculate_hours(nums, rate):
    hours=0
    for i in range(len(nums)):
        hours += math.ceil(nums[i]/rate)
    return hours

def minEatingSpeed(piles, h):
    max_element = max(piles)
    low = 1
    high = max_element

    while low<=high:
        mid = (low+high)//2
        hours = calculate_hours(piles, mid)

        if hours <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low
    
print(minEatingSpeed([30,11,23,4,20], 5))
