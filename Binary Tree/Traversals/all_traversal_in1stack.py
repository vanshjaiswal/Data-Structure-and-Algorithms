from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left =None
        self.right = None

class Solution:
    
    
    def postorder_iterative(self, root):
        preorder,inorder, postorder =[],[],[]
        stack = deque()
        
        stack.append((root,1))

        while stack:
            node, state = stack.pop()

            if state ==1:
                preorder.append(node.data)
                state=2
                stack.append((node, state))
                if node.left:
                    stack.append((node.left, 1))
            elif state == 2:
                inorder.append(node.data)
                state=3
                stack.append((node, state))
                if node.right:
                    stack.append((node.right, 1))
            else:
                postorder.append(node.data)
            
        return preorder,inorder, postorder, 

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
    pre, ino, post = solution.postorder_iterative(root)
    print("Preorder",pre) 
    print("Inorder",ino) 
    print("Postorder", post) 
