# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res = []
        if not root:
            return res
        que = deque()

        que.append(root)

        while que:
            k = len(que)
            curr_level = []

            for  _ in range(k):
                curr = que.popleft()
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)

                curr_level.append(curr.val)
            res.append(curr_level)

        return res
