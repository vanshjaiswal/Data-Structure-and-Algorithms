class Iter:

    def subset_sum_generation(self,index, arr, intermediate_list, output, subset_sum):
        if index >= len(arr):
            return output.append(subset_sum)

        # take
        intermediate_list.append(arr[index])
        subset_sum += arr[index]
        self.subset_sum_generation(index+1, arr, intermediate_list, output,subset_sum)
        

        #Not take
        intermediate_list.remove(arr[index])
        subset_sum -= arr[index]
        self.subset_sum_generation(index+1, arr, intermediate_list, output,subset_sum)
        
        
        return output


    def subsets(self,arr):
        output = []
        intermediate_list=[]
        index=0
        subset_sum=0
        if arr==[]:
            return output
        
        self.subset_sum_generation(index, arr, intermediate_list, output, subset_sum)
        return sorted(output)

sol=Iter()
arr=[1,2,1]
print(sol.subsets(arr))