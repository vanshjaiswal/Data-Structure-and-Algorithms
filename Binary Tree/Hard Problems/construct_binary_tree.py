class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    def construct_binary_tree(self, inorder, preorder, arr):
    # preorder = [3,9,20,15,7]
    # inorder = [9,3,15,20,7]
        if inorder==[] or preorder==[]:
            return None
        root=preorder[0]
        mid_index = inorder.index(root)  #1
        pre_index = len(inorder[:mid_index])  #[9]
        print(pre_index)
        
        left_inorder = inorder[:mid_index]
        print(left_inorder)
        left_preorder = preorder[1:pre_index+1]
        print(left_preorder)

        right_inorder = inorder[mid_index+1:]
        print("right", right_inorder)
        right_preorder = preorder[pre_index+1:]
        print("right", right_preorder)


        left_subtree = self.construct_binary_tree(left_inorder, left_preorder,arr)
        right_subtree = self.construct_binary_tree(right_inorder, right_preorder,arr)

        if left_subtree is None and right_subtree is None:
            arr.append(root)
        # if right_subtree is None:
        #     arr.append(root.val)
        return arr

    def binary_tree(self, inorder, preorder):
        arr=[]
        if inorder==[] or preorder==[]:
            return arr
        self.construct_binary_tree(inorder, preorder, arr)
        return arr

if __name__ == "__main__":
    solution = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    ans = solution.binary_tree(inorder, preorder)
    print("Final", ans)