from collections import deque
class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):

        m = len(image)
        n = len(image[0])
        same= image[sr][sc]
        q = deque()
        q.append((sr, sc))

        while q:
            size = len(q)
            while size > 0:
                size -= 1
                x, y = q.popleft()

                dx = [-1, 0, 0, 1]
                dy = [0, -1, 1, 0]

                for r in range(4):
                    i = x + dx[r]
                    j = y + dy[r]

                    if 0 <= i < m and 0 <= j < n and image[i][j] != color and image[i][j] == same:
                        image[i][j] = color
                        q.append((i,j))
            
        return image

        
sol = Solution()

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

ans = sol.floodFill(image, sr, sc, color)
print(ans)