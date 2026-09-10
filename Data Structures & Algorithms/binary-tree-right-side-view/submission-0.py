# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        res = []
        if not root :
            return res

        que = deque()
        que.append(root)

        level = 0
        while que:
            k = len(que)
            for  _ in range(k):
                curr = que.popleft()
                if level == len(res):
                    res.append(curr.val)
                if curr.right:
                    que.append(curr.right)
                if curr.left:
                    que.append(curr.left)
            level += 1
        return res