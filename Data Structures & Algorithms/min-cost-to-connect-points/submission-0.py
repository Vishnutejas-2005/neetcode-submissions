import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)



        self.parent = [i for i in range(n)]

        edges = []

        for i in range(n):
            for j in range(i+1,n):
                distance = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(edges,(distance,i,j))

        cost = 0

        while edges:
            d,u,v = heapq.heappop(edges)
            if self.find_parent(u)!= self.find_parent(v):
                self.union(u,v)
                cost += d

        return cost



    def find_parent(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find_parent(self.parent[x])

        return self.parent[x]

    def union(self,x,y):
        px = self.find_parent(x)
        py = self.find_parent(y)

        self.parent[px] = self.parent[py]
