class Recursion:

    def combination_sum(self, index, arr, target, intermediate, output):
        if index >= len(arr):
            return
        if target==0:
            output.append(intermediate.copy())
        #pick
        if arr[index] <= target:  #2 <= 1 ------ [2,2,2], 1
            intermediate.append(arr[index])
            # print(intermediate, target)
            self.combination_sum(index, arr, target-arr[index], intermediate, output)
            intermediate.pop()
            target +=arr[index]
        self.combination_sum(index+1, arr, target-arr[index], intermediate, output)

        return output



    def driver(self, arr, target):
        output=[]
        intermediate = []
        index = 0
        if arr==[]:
            return output
        self.combination_sum(index, arr, target, intermediate, output)
        return output

if __name__ == "__main__":
    solution = Recursion()
    arr=[8,7,4,3]
    target=11
    ans = solution.driver(sorted(arr), target)
    print(ans)