from collections import deque
class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

class  Solution:
    def ZigZagLevelOrder(self, root):
        if root is None:
            return 

        q=deque()
        q.append(root)
        ans=[]
        flag=0
        while q:
            size = len(q)
            level =[]
            node = q.popleft()
            for i in range(size): 
                if flag%2==0:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)

                    
                else:                
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                        
                level.append(node.val)

            ans.append(level)
            flag+=1
        return ans



    def zigzag2(self,root):
        ans=[]
        if root is None:
            return ans

        q=deque()
        q.append(root)
        leftToRight = True

        while q:
            size = len(q)
            level = [0] * size

           
            for i in range(size):
                node=q.popleft()
               
                if leftToRight:
                    level[i]=node.val
                else:
                    level[size-i-1]=node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            leftToRight = not leftToRight
            ans.append(level)
        return ans




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

    # Get the zigzag level order traversal
    result = solution.zigzag2(root)
    print(result)
                

