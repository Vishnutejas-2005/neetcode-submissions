class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        res = []

        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            indeg[a] += 1
            adj[b].append(a)

        que = deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                que.append(i)
                res.append(i)

        while que:
            curr = que.popleft()

            for v in adj[curr]:
                indeg[v] -= 1

                if indeg[v] == 0:
                    res.append(v)
                    que.append(v)

        if len(res) == numCourses:
            return res
        return []