"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = []
        dic = {}

        curr = head
        i = 0
        while curr:
            dic[curr] = i
            i += 1
            curr = curr.next


        curr = head
        if head:
            copy = Node(head.val)
        else:
            return None
        curr_copy = copy
        res.append(curr_copy)
        while curr.next:
            curr = curr.next
            curr_copy.next = Node(curr.val)
            curr_copy = curr_copy.next
            res.append(curr_copy)

        curr = head
        curr_copy = copy
        while curr:
            n = curr.random
            if n == None:
                curr_copy.random = None
                curr = curr.next
                curr_copy = curr_copy.next
                continue
            idx = dic[n]
            curr_copy.random = res[idx]
            curr_copy = curr_copy.next
            curr = curr.next

        return copy 
            
        



        