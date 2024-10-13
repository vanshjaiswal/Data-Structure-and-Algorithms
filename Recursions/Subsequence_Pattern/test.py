class Solution:
    def subsequence_sum1(self, index, arr, k, intermediate, recursive_sum, output):
        if recursive_sum==k:
            output.append(intermediate.copy())
            return True
        if index >= len(arr):
            return False

        #take 
        recursive_sum += arr[index]
        intermediate.append(arr[index])
        if self.subsequence_sum1(index+1, arr, k, intermediate, recursive_sum, output):
            return True

        #not take
        recursive_sum -= arr[index]
        intermediate.append(arr[index])
        if self.subsequence_sum1(index+1, arr, k, intermediate, recursive_sum, output):
            return True

        return False

    def driver(self, nums, k):
        output =[]
        intermediate = []
        index = 0
        recursive_sum=0
        self.subsequence_sum1(index,nums, k, intermediate, recursive_sum, output)
        return output

sol = Solution()
nums = [1,2,1]
k=2
ans=sol.driver(nums, k)
print(ans)