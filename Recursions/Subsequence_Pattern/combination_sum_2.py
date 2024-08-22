class Recursion:

    def combination_sum(self, index, arr, target, intermediate, output):
        if target==0:
            output.add(tuple(intermediate.copy()))
            return
        if index >= len(arr):
            return
        
       
        if arr[index] <= target:
            intermediate.append(arr[index])
            print(intermediate, target, target-arr[index])
            self.combination_sum(index+1, arr, target-arr[index], intermediate, output)
            intermediate.remove(arr[index])

        target +=arr[index]
        self.combination_sum(index+1, arr, target-arr[index], intermediate, output)

        return output


    def combination_sum2(self, index, arr, target, intermediate, output):
        if target==0:
            output.append(intermediate.copy())
            return
        if index >= len(arr):
            return 

        for i in range(index, len(arr)):
            if i>index and arr[i]==arr[i-1]:
                continue
            if arr[i] > target:
                break
            intermediate.append(arr[i])
            self.combination_sum2(i+1, arr, target-arr[i], intermediate, output)
            intermediate.remove(arr[i])
            # target += arr[i]
            # self.combination_sum2(index+i, arr, target-arr[i], intermediate, output)
        
        return output


    def driver(self, arr, target):
        output=[]
        intermediate = []
        index = 0
        if arr==[]:
            return output
        self.combination_sum2(index, sorted(arr), target, intermediate, output)
        # output  = list([list(i) for i in output])
        return output

if __name__ == "__main__":
    solution = Recursion()
    arr=[3,4,7,8]
    target=11

    arr=[10,1,2,7,6,1,5]
    target=8
    ans = solution.driver(arr, target)
    print(ans)