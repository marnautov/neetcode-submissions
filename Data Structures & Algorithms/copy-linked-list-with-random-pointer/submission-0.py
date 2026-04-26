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
        
        mapping = {}
        copy_head = Node(0)
        copy_curr = copy_head
        curr = head

        while curr:
            copy = Node(curr.val)
            mapping[curr] = copy

            copy_curr.next = copy
            copy_curr = copy_curr.next

            curr = curr.next

        curr = head
        while curr:
            copy = mapping[curr]
            copy.next = mapping.get(curr.next)
            copy.random = mapping.get(curr.random)
            curr = curr.next


        return copy_head.next