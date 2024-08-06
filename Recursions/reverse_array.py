def reverse_array(arr, start, end):
    if start==end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_array(arr, start+1, end-1)

print(reverse_array([1,2,3,4,5], 0, 4))
