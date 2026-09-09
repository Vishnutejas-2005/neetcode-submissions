class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import deque

        components = 0
        no_of_edges = len(edges)

        adj = [[] for _ in range(n)]

        visited = [False]*n

        que =deque()

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                components += 1
                que.append(i)

                while que:
                    curr = que.popleft()

                    for v in adj[curr]:
                        if visited[v] == False:
                            visited[v] = True
                            que.append(v)

        if components == 1 and no_of_edges == n-1:
            return True

        return False
         