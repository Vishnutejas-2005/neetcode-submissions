# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def same(self,p,q):
        if not p:
            if not q:
                return True
            return False
        if not q:
            return False

        if p.val != q.val:
            return False

        return self.same(p.left,q.left) and self.same(p.right,q.right)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.same(root,subRoot):
            return True

        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)