class Recursion:
    def IsPalindrome(self, s):
        if s==s[::-1]:
            return True
        else:
            return False

    def palindrome_partitioning(self, index, s, intermediate, output):
        if index == len(s):
            output.append(intermediate.copy())
            return

        
        for i in range(index, len(s)):
            if self.IsPalindrome(s[index:i+1]):
                intermediate.append(s[index:i+1])
                self.palindrome_partitioning(i+1, s, intermediate, output)
                intermediate.remove(s[index:i+1])
        return output


    def driver(self, s):
        output=[]
        intermediate = []
        index=0
        if s=="":
            return output
        self.palindrome_partitioning(index, s, intermediate, output)
        return output


if __name__ == "__main__":
    sol=Recursion()
    s="aabb"
    ans = sol.driver(s)
    print(ans)




