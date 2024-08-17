"""
In the boundary traversal it is basically divided into three parts:

1: Left Boundary
2: Bottom Traversal (Leaf Nodes)
3: Right Boundary

"""

class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Solution:

    def isLeaf(self, root):
        if root is None:
            return False
        
        if root.left == root.right == None:
            return True
        else:
            False

    def addLeftBoundary(self, root, left_boundary):
        if root is None:
            return 
        if left_boundary==[]:
            left_boundary.append(root.val)
            root = root.left

        if not self.isLeaf(root):
            left_boundary.append(root.val)
            if root.left:
                self.addLeftBoundary(root.left, left_boundary)
            if root.right:
                self.addLeftBoundary(root.right, left_boundary)
       
       
        return left_boundary

    def addRightBoundary(self, root, right_boundary):
        if root is None:
            return
        if right_boundary==[]:
            root=root.right
        
        if not self.isLeaf(root):
            right_boundary.append(root.val)
            if root.right:
                self.addRightBoundary(root.right, right_boundary)
            if root.left:
                self.addRightBoundary(root.left, right_boundary)


        return right_boundary[::-1]

    def addLeafNodes(self, root, bottom_leaf):
        #preorder: root left right
        # if root is None:
        #     return 
       
        if self.isLeaf(root):
            bottom_leaf.append(root.val)
        
        if root.left:
            self.addLeafNodes(root.left, bottom_leaf)
        if root.right:
            self.addLeafNodes(root.right, bottom_leaf)
        return bottom_leaf


    def boundary_traversal(self, root):
        left_boundary = []
        right_boundary = []
        bottom_leaf = []

        left_traversal = self.addLeftBoundary(root, left_boundary)
        right_traversal = self.addRightBoundary(root, right_boundary)
        bottom_leaf_traversal = self.addLeafNodes(root, bottom_leaf)

        ans = left_traversal + bottom_leaf_traversal + right_traversal
        return left_traversal, bottom_leaf_traversal, right_traversal, ans

if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    solution = Solution()

    # Get the boundary traversal
    left, leaf, right, ans = solution.boundary_traversal(root)

print(left)
print(leaf)
print(right)
print(ans)

        


       


        

