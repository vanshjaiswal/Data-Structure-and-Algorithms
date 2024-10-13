class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
from collections import deque
class Solution:
    def widthOfBinaryTree(self,root):
        ans=0
        q=deque()
        if root is None:
            return ans
        q.append((root, 0))

        while q:
            size = len(q)
            first=None
            last=None
            # node=q.popleft()[0]
            mmin = 0
            for i in range(size):
                element = q.popleft()
                print(element)
                current_index=element[1] - mmin
                node =  element[0]
                if i == 0:
                    first = current_index
                if i==size-1:
                    last=current_index
                
                if node.left:
                    q.append([root.left, current_index*2 + 1])
                if node.right:
                    q.append([root.right, current_index*2 +2])

            ans = max(ans, last-first+1)
        return ans

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

    sol = Solution()

    maxWidth = sol.widthOfBinaryTree(root)

    print(f"Maximum width of the binary tree is: {maxWidth}")
