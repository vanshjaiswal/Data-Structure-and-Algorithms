class Node:
    def __init__(self, data):
        self.left=None
        self.right = None
        self.data = data
    
    def insert (self, data):
        # Compare the new value with the parent node
        if self.data:
            if self.data < data:
                if self.left is None: #left node is empty
                    self.left = Node(data) #assigning the data to the left node
                else:
                    self.left.insert(data)
            elif self.data > data:
                if self.right is None: #Right node is empty
                    self.right = Node(data) #assigning the data to the right node
                else:
                    #calling the insert function again to assign the node at next level
                    self.right.insert(data) 

        else:
            self.data = data
    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()