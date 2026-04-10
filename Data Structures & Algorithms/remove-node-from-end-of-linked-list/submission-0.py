# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        remove, nxt = slow.next, slow.next.next
        slow.next = nxt

        return dummy.next