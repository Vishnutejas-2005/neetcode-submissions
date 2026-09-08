"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if node is None:
            return None

        old_new = {}
        old_new[node] = Node(node.val)

        que = deque()

        que.append(node)

        while que:
            curr = que.popleft()

            for v in curr.neighbors:
                if v not in old_new:
                    old_new[v] = Node(v.val)
                    que.append(v)

                old_new[curr].neighbors.append(old_new[v])

        return old_new[node]