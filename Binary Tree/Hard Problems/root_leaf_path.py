class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def root_leaf_path(self, root, target, arr):
        if root is None:
            return False
        arr.append(root.val)

        if root.val==target:
            return True
        
        if self.root_leaf_path(root.left, target, arr) or self.root_leaf_path(root.right, target, arr):
            return True
        
        arr.pop()
        return False
    
    def solve(self,root, target):
        arr = []
        if root is None:
            return arr
        self.root_leaf_path(root, target, arr)
        return arr



if __name__ == "__main__":
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.right.left = Node(0)
    root.right.right = Node(8)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)

    solution = Solution()
    target=7
    # arr = []
    ans=solution.solve(root, target) 
    print(ans)
        
        
