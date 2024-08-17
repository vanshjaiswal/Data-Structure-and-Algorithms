class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def diameter_check(self, root, diameter):
        if root is None:
            return 0

        LH = self.diameter_check(root.left, diameter)
        RH = self.diameter_check(root.right, diameter)

        diameter[0] = max (diameter[0], LH+RH)

        return 1+max(LH, RH)

    def diameter(self, root):
        diameter = [0]
        self.diameter_check(root, diameter)
        return diameter[0]



if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    # Creating an instance of the Solution class
    solution = Solution()

    # Calculate the diameter of the binary tree
    diameter = solution.diameter(root)
    print(diameter)