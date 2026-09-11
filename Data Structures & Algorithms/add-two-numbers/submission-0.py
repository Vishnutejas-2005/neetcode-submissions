# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        res = head
        if not l1:
            return l2
        if not l2:
            return l1

        c1 = l1
        c2 = l2
        rem = 0
        while c1 and c2:
            curr = c1.val + c2.val + rem
            res.next = ListNode(curr%10)
            rem = curr // 10

            res = res.next
            c1 = c1.next
            c2 = c2.next

        while c1:
            curr = c1.val + rem
            res.next = ListNode(curr%10)
            rem = curr//10

            res = res.next
            c1 = c1.next

        while c2 :
            curr = c2.val + rem
            res.next = ListNode(curr%10)
            rem = curr//10

            res = res.next
            c2 = c2.next

        while rem != 0:
            curr = rem
            res.next = ListNode(curr%10)
            rem = curr//10

            res = res.next

        return head.next
