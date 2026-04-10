# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next

        if not head2:
            return

        # reverse second half
        slow.next = None
        ptr, ptr2 = head2, head2.next
        head2.next = None
        while ptr and ptr2:
            p2next = ptr2.next
            ptr2.next = ptr
            ptr, ptr2 = ptr2, p2next
        head3 = ptr

        # interleave
        forward, backward = head, head3
        while forward and backward:
            fnext, bnext = forward.next, backward.next
            forward.next = backward
            backward.next = fnext
            forward, backward = fnext, bnext
            
