#We can create a node of the tree first of all

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def printTree(self):
        print(self.data)


root = Node(10) #Instatiation of the Node object
root.printTree()