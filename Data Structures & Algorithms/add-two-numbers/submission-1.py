# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            digit, carry = (val1 + val2 + carry) % 10, (val1 + val2 + carry) >= 10
            ptr.next = ListNode(digit)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            ptr = ptr.next
        
        if carry:
            ptr.next = ListNode(1)
        
        return dummy.next