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
        old_to_new = defaultdict(lambda: Node(0)) # old: new
        ptr = head
        old_to_new[None] = None
        while ptr:
            old_to_new[ptr].val = ptr.val
            old_to_new[ptr].next = old_to_new[ptr.next]
            old_to_new[ptr].random = old_to_new[ptr.random]
            ptr = ptr.next
        return old_to_new[head]