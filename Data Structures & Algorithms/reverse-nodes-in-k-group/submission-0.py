# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth: break

            groupNext = kth.next
            prev, current = groupNext, groupPrev.next
            while current != groupNext:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            
            nxt = groupPrev.next
            groupPrev.next = kth
            groupPrev = nxt

        return dummy.next

    def getKth(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1

        return current