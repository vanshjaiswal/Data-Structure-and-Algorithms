class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def balanced_check_BT(self, root):
        if root is None:
            return 0

        LH = self.balanced_check_BT(root.left)
        RH = self.balanced_check_BT(root.right)

        if abs(LH-RH)>1:
            return -1
        if LH == -1 or RH == -1:
            return -1
        
        return 1 + max(LH, RH)

    def balanced_binary_tree(self, root):
        value = self.balanced_check_BT(root)
        if value == -1:
            return False
        else:
            return True

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    solution = Solution()
    ans = solution.balanced_binary_tree(root)
    print(ans)