class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0]*9
        col = [0]*9
        box = [[0,0,0] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    curr = 1<<(int(board[i][j]))

                    if row[i] & (curr):
                        return False
                    row[i] |= (curr)

                    if col[j] &(curr):
                        return False

                    col[j] |= (curr)

                    if box[i//3][j//3] &(curr):
                        return False
                    box[i//3][j//3] |= (curr)

        return True