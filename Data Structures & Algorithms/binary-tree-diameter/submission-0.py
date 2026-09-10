# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def d(self,r):
        if not r:
            return (-1,-1,0)
        l1,r1,m1,l2,r2,m2 = 0,0,0,0,0,0

        l1,r1,m1 = self.d(r.left)
        l2,r2,m2 = self.d(r.right)

        l = 1 + max(l1,r1)
        ri = 1 + max(l2,r2)

        m =  max(l+ri,m1,m2)

        return l,ri,m
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l,r,m = self.d(root)
        return max(l+r,m)