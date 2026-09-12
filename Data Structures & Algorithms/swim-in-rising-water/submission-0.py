import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        pq = [(grid[0][0],0,0)]
        dir = [
            (0,1),
            (1,0),
            (-1,0),
            (0,-1)
        ]
        visited = set()
        while pq:
            time,x,y = heapq.heappop(pq)

            if (x,y) in visited:
                continue

            visited.add((x,y))

            if x == n-1 and y == n-1:
                return time

            for dx,dy  in dir:
                nx = x+dx
                ny = y + dy

                if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited:
                    new_time = max(time,grid[nx][ny])
                    heapq.heappush(pq,(new_time,nx,ny))
                    
