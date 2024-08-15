from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def preorder_iterative(self, root):
        preorder = []
        
        stack = deque()
        if not root:
            return preorder

        stack.append(root)

        while stack:
            node  = stack.pop()
            preorder.append(node.data)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return preorder


# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Create an instance
    # of the Solution class
    solution = Solution()
    # Perform level-order traversal
    result = solution.preorder_iterative(root)
    print(result)
            



