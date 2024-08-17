class Node:
    def __init__(self, val):
        self.val = val
        self.left=None
        self.right=None

    
class Solution:
    def maximum_path_sum(self, root, max_sum):
        if root is None:
            return 0

        LeftSum = max(0,self.maximum_path_sum(root.left, max_sum))
        RightSum = max(0,self.maximum_path_sum(root.right, max_sum))
      

        max_sum[0]=max(max_sum[0], (LeftSum + RightSum + root.val))

        return root.val + max(LeftSum, RightSum)

    def max_sum(self, root):
        max_sum=[float("-inf")]
        self.maximum_path_sum(root, max_sum)
        return max_sum[0]

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Finding and printing the maximum path sum
    maxPathSum = solution.max_sum(root)
    print("Maximum Path Sum:", maxPathSum)

