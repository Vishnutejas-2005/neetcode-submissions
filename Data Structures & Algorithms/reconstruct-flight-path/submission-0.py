from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for u,v in tickets:
            adj[u].append(v)

        scr = "JFK"
        for u in adj:
            adj[u].sort(reverse=True)
        ans =[]
        
        def dfs(scr):
            while adj[scr]:
                curr = adj[scr].pop()
                dfs(curr)

            ans.append(scr)

        dfs(scr)
        return ans[::-1]