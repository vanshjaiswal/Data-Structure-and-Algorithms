"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 
 Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

https://takeuforward.org/data-structure/merge-overlapping-sub-intervals/
"""

def merge_brute(intervals):
    n = len(arr) # size of the array

    # sort the given intervals:
    arr.sort()

    ans = []

    for i in range(n): # select an interval:
        start, end = arr[i][0], arr[i][1]

        # Skip all the merged intervals:
        if ans and end <= ans[-1][1]:
            continue

        # check the rest of the intervals:
        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])
    return ans



#optimal

def merge_optimal(intervals):
    n = len(intervals) # size of the array

    # sort the given intervals:
    intervals.sort()

    ans = []

    for i in range(n):
        # if the current interval does not
        # lie in the last interval:
        if not ans or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
        # if the current interval
        # lies in the last interval:
        else:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
    return ans

# print(merge( [[1,3],[2,6],[8,10],[15,18]]))
# print(merge([[1,4],[4,5]]))
# print(merge([[1,4],[0,4]]))
print(merge_optimal([[1,4],[2,3]]))


        
