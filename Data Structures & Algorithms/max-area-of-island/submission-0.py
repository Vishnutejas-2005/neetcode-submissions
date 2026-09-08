class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        n = len(grid)
        m = len(grid[0])

        dir = [(0,1),(1,0),(0,-1),(-1,0)]

        que = deque()

        max_area = 0

        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == False:
                    visited[i][j] = True
                    que.append((i,j))
                    curr_area = 0

                    while que:
                        x,y = que.popleft()
                        curr_area += 1

                        for dx,dy in dir:
                            nx = x + dx
                            ny = y + dy

                            if 0<=nx<n and 0<= ny <m and grid[nx][ny] == 1 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                que.append((nx,ny))
                    max_area = max(max_area,curr_area)
        return max_area