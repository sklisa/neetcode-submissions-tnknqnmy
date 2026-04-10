# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ptr1, ptr2 = head, head.next
        ptr1.next = None
        while ptr2 != None:
            p2next = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = p2next
        return ptr1