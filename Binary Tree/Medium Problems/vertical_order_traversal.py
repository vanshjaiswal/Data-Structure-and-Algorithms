"""

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.


"""

from collections import deque
class Node:
    def __init__(self, val):
        self.val=val
        self.left = None
        self.right = None
    
class Solution:
    def vertical_traversal(self, root):
        q=deque()
        inter_dic={}
        q.append([root, [0, 0]])

        while q:
            size = len(q)
            # inter_dic = {}
            for i in range(size):
                element = q.popleft()
                node=element[0]
                vertical = element[1][0]
                level = element[1][1]
                if vertical in inter_dic.keys():
                    if level in inter_dic[vertical].keys():
                        inter_dic[vertical][level].append(node.val)
                    else:
                        inter_dic[vertical][level] = [node.val]#{level:[node.val]}
                else:
                    inter_dic[vertical] = {level:[node.val]}

                if node.left:
                    q.append([node.left, [vertical-1, level+1]])
                if node.right:
                    q.append([node.right, [vertical+1, level+1]])

        dic_keys = list(inter_dic.keys())
        dic_keys = sorted(dic_keys)
        inter_dic2 = {i: inter_dic[i] for i in dic_keys}
        ans=[]
        print(inter_dic2)
        for i in inter_dic2:
            ls=[]
            for j in inter_dic2[i]:
                ls=ls + sorted(inter_dic2[i][j])
                
            ans.append(ls)

        return ans


if __name__ == "__main__":
    # Creating a sample binary tree
    # root = Node(1)
    # root.left = Node(2)
    # root.left.left = Node(4)
    # root.left.right = Node(10)
    # root.left.left.right = Node(5)
    # root.left.left.right.right = Node(6)
    # root.right = Node(3)
    # root.right.right = Node(10)
    # root.right.left = Node(9)

    solution = Solution()

    # Get the Vertical traversal
    # verticalTraversal = solution.vertical_traversal(root)
    # # print(verticalTraversal)
    # 1234567
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    root.right.right = Node(7)
    root.right.left = Node(6)
    
    verticalTraversal = solution.vertical_traversal(root)
    print(verticalTraversal)


        