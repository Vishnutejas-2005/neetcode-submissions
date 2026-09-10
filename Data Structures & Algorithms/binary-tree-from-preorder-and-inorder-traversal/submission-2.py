# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.dic = {value:i for i,value in enumerate(inorder)}

        def build(ps,pe,i_s,ie):
            if ps > pe:
                return None

            v = preorder[ps]
            root = TreeNode(v)

            i = self.dic[v]

            length = i-i_s

            root.left = build(ps+1,ps+length,i_s,i-1)
            root.right = build(ps+length+1,pe,i+1,ie)

            return root

        return build(0,len(preorder)-1,0,len(preorder)-1)