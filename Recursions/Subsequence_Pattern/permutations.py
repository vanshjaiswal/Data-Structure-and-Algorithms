class Recursion:
    def permutation(self, arr, intermediate, dic, output):
        if len(intermediate) == len(arr):
            output.append(intermediate.copy())
            return
        for i in range(0, len(arr)):
            if dic[i]==0:
                intermediate.append(arr[i])
                dic[i]=1
                self.permutation(arr, intermediate, dic, output)
                intermediate.remove(arr[i])
                dic[i]=0

        return output



    def driver(self, arr):
        output=[]
        intermediate = []
        ind_list = list(range(len(arr)))
        dic = dict(zip(ind_list, [0]*len(arr)))

        self.permutation(arr, intermediate, dic, output)
        return output

sol = Recursion()
arr=[1,2,3]
ans = sol.driver(arr)
print(ans)