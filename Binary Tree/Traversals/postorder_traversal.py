"""
postorder traversal(left, right, root) in binary tree
"""

#creating the node of the tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
#Creating a postorder traversal function

def postorder(root, arr):
    #base case for recursion, if further node is not present it will return back
    if not root:
        return
    #now we will recursively call the postorder function to get the right node values
    postorder(root.left, arr)
    postorder(root.right, arr)
    #if the node is present then we will store the data of the node
    arr.append(root.data) 
    return arr

if __name__== "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    arr=[]
    result = postorder(root, arr)
    print(result)