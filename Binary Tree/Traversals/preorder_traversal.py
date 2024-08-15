"""
preorder traversal(root, left, right) in binary tree
"""

#creating the node of the tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
#Creating a preorder traversal function

def preorder(root, arr):
    #base case for recursion, if further node is not present it will return back
    if not root:
        return

    #if the node is present then we will store the data of the node
    arr.append(root.data) 

    #now we will recursively call the preorder function to get the left and right node values
    preorder(root.left, arr)
    preorder(root.right, arr)

    return arr

if __name__== "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    arr=[]
    result = preorder(root, arr)
    print(result)