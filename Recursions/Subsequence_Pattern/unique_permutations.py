"""
https://leetcode.com/problems/permutations-ii/submissions/1365799094/

"""

class Recursion:
    def permutation(self, arr, intermediate, dic, output):
        if len(intermediate) == len(arr):
            # output.add(tuple(intermediate.copy()))
            output.append(intermediate.copy())
            return
        for i in range(0, len(arr)):
            # if arr[i]==arr[i-1]:
            #     continue
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
        if arr==[]:
            return []
        ind_list = list(range(len(arr)))
        dic = dict(zip(ind_list, [0]*len(arr)))

        self.permutation(arr, intermediate, dic, output)

        output = set((tuple(i) for i in output))
        
        return output

sol = Recursion()
arr=[2,2,1,1]
ans = sol.driver(arr)
print(ans)