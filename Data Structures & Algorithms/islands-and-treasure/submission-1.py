class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        n = len(grid)
        m = len(grid[0])

        dir = [(0,1),(1,0),(-1,0),(0,-1)]


        que = deque()
        inf = 2147483647

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    que.append((i,j))


        while que:
            x,y = que.popleft()
            for dx,dy in dir:
                nx= x +dx
                ny = y  +dy
                if 0 <= nx<n and 0<=ny<m and grid[nx][ny] == inf:
                    grid[nx][ny] = grid[x][y] + 1
                    que.append((nx,ny))
