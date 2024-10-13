class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def LCA(self, root, p, q):
        path_p = set(self.path_finder(root, p))
        path_q = set(self.path_finder(root, q))

        lca = list(path_p.intersection(path_q))
        # print(path_p)
        # print(path_q)
        # print(lca)
        return min(lca)

    def root_leaf_path(self, root, target, arr):
        if root is None:
            return False
        
        arr.append(root.val)
        if root.val==target:
            return True
        
        if self.root_leaf_path(root.left, target, arr) or self.root_leaf_path(root.right, target, arr):
            return True
        
        arr.pop()
        return False
    
    def path_finder(self, root, target):
        arr=[]
        if root is None:
            return arr

        self.root_leaf_path(root, target, arr)
        return arr


    def lowestCommonAncestor(self, root, p, q):
        # if root is None or root==p or root==q:
        #     return root
        
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left is None:
        #     return right
        # elif right is None:
        #     return left
        # else:
        #     return root 

        if not root or root == p or root == q:
            return root                                                                           

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r



# root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.right.left = Node(0)
    root.right.right = Node(8)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)

    solution = Solution()
    p=5
    q=1
    # arr = []
    ans=solution.LCA(root, p,q) 
    print(ans)