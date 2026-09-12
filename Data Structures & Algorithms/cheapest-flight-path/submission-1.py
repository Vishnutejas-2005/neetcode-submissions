class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = 10**18
        cost = [inf]*n

        cost[src] = 0

        for _ in range(k+1):

            new_cost = cost.copy()

            for u,v,w in flights:
                if cost[u] != inf:
                    new_cost[v] = min(new_cost[v],cost[u]+w)

            cost = new_cost

        if cost[dst] != inf:
            return cost[dst]

        return -1