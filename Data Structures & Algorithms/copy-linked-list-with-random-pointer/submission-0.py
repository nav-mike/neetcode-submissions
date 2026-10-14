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
        buffer = {None: None}

        pointer = head
        while pointer:
            buffer[pointer] = Node(pointer.val)
            pointer = pointer.next
        
        pointer = head
        while pointer:
            buffer[pointer].next = buffer[pointer.next]
            buffer[pointer].random = buffer[pointer.random]
            pointer = pointer.next
        
        return buffer[head]
        