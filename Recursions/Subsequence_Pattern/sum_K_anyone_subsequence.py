class Recursion:
    def anyone_sum_k(self, index, arr, intermediate_list, recursive_sum, k, output):
        if index >= len(arr):
            if recursive_sum==k:
                output.append(intermediate_list.copy())
                return True
            else:
                return False

        intermediate_list.append(arr[index])
        recursive_sum +=arr[index]
        if self.anyone_sum_k(index+1, arr, intermediate_list, recursive_sum, k, output):
            return True

        intermediate_list.remove(arr[index])
        recursive_sum -=arr[index]
        if self.anyone_sum_k(index+1, arr, intermediate_list, recursive_sum, k, output):
            return True

        return output    

    def driver(self, arr, k):
        output = []
        recursive_sum=0 
        intermediate_list=[]
        index=0
        if arr == []:
            return output
        self.anyone_sum_k(index, arr, intermediate_list, recursive_sum, k, output)
        return output   



    def count_sum_k(self, index, arr, recursive_sum, k):
        if index >= len(arr):
            if recursive_sum==k:
                return 1
            else:
                return 0

        recursive_sum +=arr[index]
        l = self.count_sum_k(index+1, arr, recursive_sum, k)

        recursive_sum-=arr[index]
        r = self.count_sum_k(index+1, arr, recursive_sum, k)

        return l + r
        
    def count(self, arr, k):
        recursive_sum = 0
        index = 0
        if arr==[]:
            return 0
        output = self.count_sum_k(index, arr, recursive_sum, k)
        return output


solution = Recursion()
counter = solution.count([1,2,1,3,4,5], 5)
print(counter)
ans=solution.driver([1,2,1],2)
print(ans)

counter = solution.count([1,2,1], 2)
print(counter)


