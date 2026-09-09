class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(n+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x,y):
            px = find(x)
            py = find(y)

            if px == py:
                return False

            parent[px] = py

            return True

        for u,v in edges:
            if union(u,v) == False:
                return [u,v]
            
