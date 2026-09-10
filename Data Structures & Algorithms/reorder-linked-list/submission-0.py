# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            n = curr.next
            curr.next = prev

            prev = curr
            curr = n

        res = head
        h1 = head
        h2 = prev

        while h1 and h2:
            n1 = h1.next
            n2 = h2.next

            h1.next = h2
            h2.next = n1

            h1 = n1
            h2 = n2

        # return res
        
