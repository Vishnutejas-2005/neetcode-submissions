# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root:
            return ""
        def dfs_s(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs_s(root.left)
            dfs_s(root.right)
        dfs_s(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        values = data.split(",")

        self.i = 0

        def dfs():
            val = values[self.i]
            self.i += 1

            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

        
