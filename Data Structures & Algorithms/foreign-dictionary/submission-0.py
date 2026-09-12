from collections import defaultdict,deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        indeg = defaultdict(int)
        adj = defaultdict(list)

        letter  = set()
        for i in range(n):
            letter |= set(words[i])
        for i in range(1,n):
            
            k = min(len(words[i-1]),len(words[i]))
            found = False
            for j in range(k):
                if words[i-1][j]!=words[i][j]:
                    adj[words[i-1][j]].append(words[i][j])
                    indeg[words[i][j]] += 1
                    found = True
                    break
            if found == False and len(words[i-1]) > len(words[i]):
                return ""


        que = deque()
        res = ""
        for l in letter:
            if indeg[l]  == 0:
                que.append(l)
                res += l

        while que:
            u = que.popleft()
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    que.append(v)
                    res += v

        if len(letter) == len(res):
            return res
        return ""

        