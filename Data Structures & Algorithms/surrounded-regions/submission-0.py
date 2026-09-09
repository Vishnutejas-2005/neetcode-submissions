class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
        n = len(board)
        m = len(board[0])

        visited = [[False for _ in range(m)] for _ in range(n)]
        que = deque()
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and visited[i][j] == False:
                    visited[i][j] = True
                    que.append((i,j))
                    curr = []
                    flag = 0
                    while que:
                        x,y = que.popleft()
                        curr.append((x,y))
                        if x == 0 or x == n-1 or y == 0 or y == m-1:
                            flag = 1

                        for dx,dy in dir :
                            nx = x + dx
                            ny = y  +dy
                            if 0<=nx<n and 0 <=ny<m and board[nx][ny] == "O" and visited[nx][ny] == False:
                                que.append((nx,ny))
                                visited[nx][ny] = True
                    if flag == 0:
                        for a,b in curr:
                            board[a][b] = "X"
        

