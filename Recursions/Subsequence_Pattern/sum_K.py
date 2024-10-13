class Recursion:
    def sum_k(self, index, arr, k,intermediate_list, recursive_sum, output):

        if recursive_sum==k:
            return output.add(tuple(intermediate_list.copy()))

        if index >=len(arr):
            return 

        #take 
        intermediate_list.append(arr[index])
        recursive_sum +=arr[index]
        self.sum_k(index+1, arr, k,intermediate_list, recursive_sum, output)

        #not take
        intermediate_list.remove(arr[index])
        recursive_sum -=arr[index]
        self.sum_k(index+1, arr, k,intermediate_list, recursive_sum, output)
        return output



    def driver(self, arr, k):
        output = set()
        recursive_sum=0 
        intermediate_list=[]
        index=0
        if arr == []:
            return output
        self.sum_k(index, arr, k,intermediate_list, recursive_sum, output)
        # output = list([list(i) for i in output])

        return output

    
solution = Recursion()
ans=solution.driver([14,6,25,9,32], 27)
print(ans)