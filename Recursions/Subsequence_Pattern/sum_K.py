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
ans=solution.driver([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12], 27)
print(ans)