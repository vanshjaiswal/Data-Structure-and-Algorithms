from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left =None
        self.right = None

class Solution:
    def postorder_iterative(self, root):

        st1 = deque()
        st2 = deque()

        st1.append(root)

        while st1:
            node = st1.pop()
            st2.append(node.data)

            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)


        result = []
        while st2:
            result.append(st2.pop())
        return result

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
    result = solution.postorder_iterative(root)
    print(result) 
