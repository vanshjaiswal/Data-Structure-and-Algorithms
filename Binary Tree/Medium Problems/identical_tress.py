class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        return (p.val == q.val 
                and self.isSameTree(p.left,q.left)
                and self.isSameTree(p.right, q.right))
       


  

if __name__ == "__main__":
    # Creating nodes for binary trees in Python
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)

    # Creating an instance of the Solution class
    solution = Solution()

# Checking if the binary trees are identical
    ans = solution.isSameTree(root1, root2)
    print(ans)
