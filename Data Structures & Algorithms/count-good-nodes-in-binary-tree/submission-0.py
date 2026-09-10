# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque
        res = 0

        if not root:
            return 0

        que = deque()
        que.append((root,root.val))

        while que:
            curr,max_ = que.popleft()
            if curr.val >= max_:
                res += 1
                max_  = curr.val
            if curr.left:
                que.append((curr.left,max_))
            if curr.right:
                que.append((curr.right,max_))

        return res