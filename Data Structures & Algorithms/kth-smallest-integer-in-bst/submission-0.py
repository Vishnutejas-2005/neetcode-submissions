# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        from collections import deque
        count = 0
        st = deque()

        st.append((root,0))

        while st:
            curr,state = st.pop()
            if state == 0:
                left = curr.left
                st.append((curr,1))
                if left:
                    st.append((left,0))
            else:
                if count == k-1:
                    return curr.val
                count += 1
                if curr.right:
                    st.append((curr.right,0))
            