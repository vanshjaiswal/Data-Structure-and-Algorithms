from collections import deque

class Node:
    def __init__ (self, data):
        self.data = data
        self.left=None
        self.right=None

class Solution:
    def height_binary_tree(self, root):

        if root is None:
            return 0

        ans=[]
        count=0
        q=deque()
        q.append(root)

        while q:
            size = len(q)
            level =[]

            for i in range(size):
                
                node = q.popleft()
                level.append(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count+=1
            ans.append(level)  
        return ans, len(ans), count

# Creating a sample binary tree
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)

    solution = Solution()
    ans, arr_len, depth = solution.height_binary_tree(root)


print(ans)
print(arr_len)
print(depth)
