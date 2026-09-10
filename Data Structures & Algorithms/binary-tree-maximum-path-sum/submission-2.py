# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,node):
        if not node:
            return 0,float("-inf")

        left,lm = self.helper(node.left)
        right,rm = self.helper(node.right)

        left = max(0,left)
        right = max(0,right)
        return node.val + max(left,right),max(lm,rm,node.val+left+right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right and not root.left:
            return root.val
        a,b = self.helper(root)
        return max(a,b)
        