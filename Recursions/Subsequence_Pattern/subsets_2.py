class Solution:
    def subsets(self, index, nums, intermediate, output):
        output.append(intermediate.copy())
        if index >= len(nums):
            return 

        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i-1]:
                continue
            intermediate.append(nums[i])
            self.subsets(i+1, nums, intermediate, output)
            intermediate.remove(nums[i])
        return output

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        intermediate = []
        index = 0
        if nums==[]:
            return output

        self.subsets(index, sorted(nums), intermediate, output)
        # output = list([list(i) for i in output])
        return output
        