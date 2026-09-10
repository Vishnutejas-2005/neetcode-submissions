class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        cols = set()
        diag1 = set()
        diag2 = set()

        def back(i):
            if i == n:
                res.append(["".join(r) for r in board])

            for c in range(n):
                if c in cols:
                    continue

                if i-c in diag1:
                    continue
                if i+c in diag2:
                    continue


                board[i][c] = "Q"
                cols.add(c)
                diag1.add(i-c)
                diag2.add(i+c)

                back(i+1)

                board[i][c] = "."
                cols.discard(c)
                diag1.discard(i-c)
                diag2.discard(i+c)

        back(0)
        return res