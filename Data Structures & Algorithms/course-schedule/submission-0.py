class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        count = 0
        indeg = [0]*numCourses

        adj = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            indeg[b] += 1
            adj[a].append(b)

        que =deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                que.append(i)
                count += 1

        while que:
            curr = que.popleft()

            for v in adj[curr]:
                indeg[v] -=1

                if indeg[v] == 0:
                    que.append(v)
                    count += 1

        return count == numCourses

        