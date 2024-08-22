"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


class Iter:

    def subset_generation(self,index, arr, intermediate_list, output):
        if index >= len(arr):
            return output.append(intermediate_list.copy())

        # take
        intermediate_list.append(arr[index])
        self.subset_generation(index+1, arr, intermediate_list, output)
        

        #Not take
        intermediate_list.remove(arr[index])
        self.subset_generation(index+1, arr, intermediate_list, output)
        
        
        return output



    def subset_generation2(self,index, arr, intermediate_list, output):
        if index >= len(arr):
            output.add(tuple(intermediate_list.copy()))
            return 
        
        intermediate_list.append(arr[index])
        self.subset_generation2(index+1, arr, intermediate_list, output)

        intermediate_list.remove(arr[index])
        self.subset_generation2(index+1, arr, intermediate_list, output)

        return output

    def subsets(self,arr):
        output = []
        intermediate_list=[]
        index=0
        if arr==[]:
            return output
        
        self.subset_generation(index, arr, intermediate_list, output)
        return output

    def subsets2(self,arr):
        output = set()
        intermediate_list=[]
        index=0
        if arr==[]:
            return output
        
        self.subset_generation2(index, arr, intermediate_list, output)
        output = list([list(i) for i in output])
        return output

sol=Iter()
arr=[1,2,2]
print(sol.subsets2(arr))