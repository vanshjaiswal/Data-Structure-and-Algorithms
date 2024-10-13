class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right =None
from collections import deque
class Solution:
    def right_view(self,root):
        arr=[]
        if root is None:
            return arr

        q=deque()
        q.append(root)

        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            arr.append(level[-1])

        return arr

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(10)
    root.left.left.right = Node(5)
    root.left.left.right.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(10)
    root.right.left = Node(9)

    solution = Solution()

    # Get the Right View traversal
    rightView = solution.right_view(root)
    print(rightView)