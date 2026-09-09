class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import deque
        components = 0

        adj = [[] for _ in range(n)]
        visited = [False]*n

        for a,b in edges:
            adj[b].append(a)
            adj[a].append(b)

        que = deque()

        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                que.append(i)
                components += 1

                while que:
                    curr = que.popleft()

                    for v in adj[curr]:
                        if visited[v] == False:
                            visited[v] = True
                            que.append(v)

        return components