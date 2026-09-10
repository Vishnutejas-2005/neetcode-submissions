class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = [False]
        l = len(word)
        n = len(board)
        m = len(board[0])
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        def back(i,x,y,visited):
            if i == l:
                return True

            for dx,dy in dir:
                nx = x + dx
                ny = y  +dy
                if 0<=nx<n and 0<=ny<m and (nx,ny) not in visited and word[i] == board[nx][ny]:
                    visited.add((nx,ny))
                    if back(i+1,nx,ny,visited):
                        return True
                    visited.discard((nx,ny))

        for a in range(n):
            for b in range(m):
                if board[a][b] == word[0]:
                    visited = set()
                    visited.add((a,b))
                    if back(1,a,b,visited):
                        return True
                    

        return False