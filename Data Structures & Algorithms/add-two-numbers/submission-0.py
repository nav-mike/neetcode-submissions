# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result = ListNode()

        ol = 0
        while l1 and l2:
            val = l1.val + l2.val + ol
            if val >= 10: ol = 1

            dummy.next = ListNode(val % 10)

            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        
        if ol > 0:
            dummy.next = ListNode(ol)

        return result.next