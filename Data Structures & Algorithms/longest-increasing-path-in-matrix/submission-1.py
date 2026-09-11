class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0 for _ in range(m)]for _ in range(n)]
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(i,j):
            if dp[i][j] != 0:
                return dp[i][j]

            dp[i][j] = 1

            for di,dj in dir:
                ni = i+di
                nj = j + dj

                if 0<=ni<n and 0<=nj<m and matrix[i][j] < matrix[ni][nj]:
                    dp[i][j] = max(dp[i][j],1+dfs(ni,nj))

            return dp[i][j]

        ans = 0

        for r in range(n):
            for c in range(m):
                ans = max(ans,dfs(r,c))

        return ans
