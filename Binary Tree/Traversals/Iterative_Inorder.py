from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def inorder_iterative(self, root):
        inorder = []
        
        stack = deque()
        node = root
        if not root:
            return inorder

        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            elif(stack):
                node = stack.pop()
                inorder.append(node.data)
                node = node.right
            else:
                break

        return inorder


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
    result = solution.inorder_iterative(root)
    print(result)
            



