"""
 Given a sorted array of N integers and an integer x, write a program to find the lower bound of x.

 The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.


"""

#optimal

def lower_bound(arr, x):
    low=0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid + 1
        
    return ans


print(lower_bound([3, 5, 8, 15, 19], 5))


#upper bound

def upper_bound(arr, x):
    low=0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid + 1
            
        
    return ans

print(upper_bound([3,5,8,9,15,19], 9))