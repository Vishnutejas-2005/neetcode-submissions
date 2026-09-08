class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        from collections import deque
        def bfs(start,n,m):
            visited = set()
            que = deque()

            dir = [(0,1),(1,0),(0,-1),(-1,0)]
            for i in start:
                visited.add(i)
                que.append(i)


            while que:
                x,y = que.popleft()

                for dx,dy in dir:
                    nx = x + dx
                    ny = y + dy

                    if 0<=nx<n and 0<=ny<m:
                        if (nx,ny) not in visited and heights[nx][ny] >= heights[x][y]:
                            visited.add((nx,ny))
                            que.append((nx,ny))

            return visited

        n = len(heights)
        m = len(heights[0])


        pacific_start = []

        for i in range(n):
            pacific_start.append((i,0))

        for j in range(1,m):
            pacific_start.append((0,j))

        atlantic_start = []

        for i in range(n):
            atlantic_start.append((i,m-1))

        for j in range(m-1):
            atlantic_start.append((n-1,j))

        p = bfs(pacific_start,n,m)
        a = bfs(atlantic_start,n,m)

        return list(p.intersection(a))