# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None

        def merge(node1, node2):
            head = ListNode()
            ptr = head

            while node1 and node2:
                if node1.val <= node2.val:
                    ptr.next = node1
                    node1 = node1.next
                else:
                    ptr.next = node2
                    node2 = node2.next
                ptr = ptr.next
            
            if not node1:
                ptr.next = node2
            
            if not node2:
                ptr.next = node1
            
            return head.next
            

        curr = lists
        while len(curr) > 1:
            temp = []
            for j in range(0, len(curr), 2):
                if j < len(curr)-1:
                    temp.append(merge(curr[j], curr[j+1]))
                else:
                    temp.append(curr[j])
            curr = temp
        
        return curr[0]
        