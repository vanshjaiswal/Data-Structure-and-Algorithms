from collections import deque
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class Solution:
    def levelOrder(self, root):
        ans = []
        #base case 
        if not root:
            return ans

        #create a queue structure for storing the current level node
        q = deque()

        #enque the root element
        q.append(root)
        
        while q:
            #get the current size of the queue
            size = len(q)

            #create a list to store the elements of that level
            level = []

            #itereate through size for the number of nodes at that level
            for i in range(size):
                #pop the left most element of the queue and add it
                #to the level list then check the left and right child
                #if they exist then add them into the queue
                node = q.popleft()
                level.append(node.data)

                #check the left and right child
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            #store the current level into the final answer
            ans.append(level)
        return ans

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Create an instance
    # of the Solution class
    solution = Solution()
    # Perform level-order traversal
    result = solution.levelOrder(root)
    print(result)




