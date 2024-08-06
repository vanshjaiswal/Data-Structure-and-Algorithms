def second_largest(arr):
    largest=float("-inf")
    second_largest=float("-inf")
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        if i > second_largest and i<largest:
            second_largest=i
    if largest==second_largest:
        return -1
    else:
        return second_largest


print(second_largest([32011, 123, 1045, 1205, 254, 28763, 6537, 3161]))
            
