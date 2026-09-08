class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        m = len(grid[0])

        dir = [(0,1),(1,0),(-1,0),(0,-1)]

        que = deque()
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    que.append((i,j))
                    count += 1
                elif grid[i][j] == 1:
                    count += 1

        rotten_count = 0
        t = -1
        while que:
            k = len(que)
            t += 1
            for _ in range(k):
                x,y = que.popleft()
                rotten_count += 1
                for dx,dy in dir:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<n and 0<=ny<m:
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            que.append((nx,ny))
        if count == 0:
            return 0
        if rotten_count == count:
            return t
        
        return -1