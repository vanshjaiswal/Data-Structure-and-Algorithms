def sorted_array(arr):
    if len(arr)<=1:
        return True
    
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:
            continue
        else:
            return False
    return True


print(sorted_array([1,2,3,4,5]))

