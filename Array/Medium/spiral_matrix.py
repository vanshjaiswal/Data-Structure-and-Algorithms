"""
https://takeuforward.org/data-structure/spiral-traversal-of-matrix/

https://leetcode.com/problems/spiral-matrix/description/

Example 1:
Input: Matrix[][] = { { 1, 2, 3, 4 },
		      { 5, 6, 7, 8 },
		      { 9, 10, 11, 12 },
	              { 13, 14, 15, 16 } }

Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
Explanation: The output of matrix in spiral form.
[[1,2,3],[4,5,6],[7,8,9]]
[1,2,3,6,9,8,7,4,5]

"""

def spiral(matrix):

    ans=[]
    n=len(matrix) #number of rows
    m=len(matrix[0]) #number of columns

    #row tag
    top=0
    bottom = n-1

    #column tag
    left = 0
    right =  m-1

    while top<=bottom and left <= right:
        #printing left to right row
        for i in range(left, right+1):
            ans.append(matrix[top][i])
        top +=1
        print(ans)

        #printing top to bottom
        for i in range(top, bottom+1):
            ans.append(matrix[i][right])
        right-=1
        print(ans)
        #print right to left
        if (top <= bottom):
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
            bottom-=1
        print(ans)
        #print bottom to top
        if (left <= right):
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
            left+=1
        print(ans)

    return ans

print(spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
        
