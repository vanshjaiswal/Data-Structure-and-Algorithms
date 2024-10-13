def longest_divisible_subset(arr):
    n = len(arr)

    # Sort the array in ascending order
    arr.sort()

    # Initialize dp and hash arrays with 1s
    dp = [1] * n
    hash_arr = list(range(n))

    # Iterate through the array
    for i in range(n):
        for prev_index in range(i):
            if arr[i] % arr[prev_index] == 0 and 1 + dp[prev_index] > dp[i]:
                dp[i] = 1 + dp[prev_index]
                hash_arr[i] = prev_index

    ans = -1
    last_index = -1

    # Find the maximum length and its corresponding index
    for i in range(n):
        if dp[i] > ans:
            ans = dp[i]
            last_index = i
    # print(dp)
    # print(last_index)

    # Reconstruct the divisible subset
    result = [arr[last_index]]

    while hash_arr[last_index] != last_index:
        last_index = hash_arr[last_index]
        result.append(arr[last_index])

    return result

def largestDivisibleSubset(nums):
    n = len(nums)

    dp = [1] * n
    hash = list(range(n))
    nums.sort()

    for ind in range(n):
        for prev in range(ind):
            if nums[ind] % nums[prev] ==0 and ((1 + dp[prev]) > dp[ind]):
                dp[ind] = 1 + dp[prev]
                hash[ind] = prev

    ans = max(dp)
    last_index=nums.index(4)

    print(dp)
    print(max(dp))
    print(last_index)

    result = [nums[last_index]]

    while hash[last_index] != last_index:
        last_index = hash[last_index]
        result.append(nums[last_index])

    return result   


# print(longest_divisible_subset([1,2,4,8]))
print(largestDivisibleSubset([1,2,4,8]))