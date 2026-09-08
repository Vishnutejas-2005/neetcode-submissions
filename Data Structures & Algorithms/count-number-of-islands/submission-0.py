
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        n = len(grid)
        m = len(grid[0])
        visited = set()

        que = deque()
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i,j))
                    que.append((i,j))
                    count += 1
                    while que:
                        x,y = que.popleft()
                        for dx,dy in dir:
                            nx  = x + dx
                            ny = y  + dy
                            if 0 <= nx<n and 0 <= ny <m and grid[nx][ny] == "1" and (nx,ny) not in visited :
                                visited.add((nx,ny))
                                que.append((nx,ny))

        return count
