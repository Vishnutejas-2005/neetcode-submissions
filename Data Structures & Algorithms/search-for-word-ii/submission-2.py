class prefixtree:
    def __init__(self):
        self.children = {}
        self.wor = None

    def set(self,word):
        curr =self

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = prefixtree()

            curr = curr.children[ch]

        curr.wor = word

    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = prefixtree()
        for word in words:
            tree.set(word)

        res = []
        visited = set()
        n = len(board)
        m = len(board[0])
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        def back_track(curr_node,x,y):
            if curr_node.wor:
                res.append(curr_node.wor)
                curr_node.wor = None


            for dx,dy in dir:
                nx = x  +dx
                ny = y + dy

                if 0<=nx<n and 0 <= ny<m and (nx,ny) not in visited:
                    ch = board[nx][ny]
                    if ch in curr_node.children:
                        visited.add((nx,ny))
                        back_track(curr_node.children[ch],nx,ny)
                        visited.discard((nx,ny))

        for i in range(n):
            for j in range(m):
                ch = board[i][j]

                if ch in tree.children:
                    visited.add((i,j))
                    back_track(tree.children[ch],i,j)
                    visited.discard((i,j))

        return res
            
            

            