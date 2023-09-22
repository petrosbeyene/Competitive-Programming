# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lh = left_head = ListNode()
        rh = right_head = ListNode()

        while head:
            if head.val < x:
                left_head.next = head
                left_head = head
            else:
                right_head.next = head
                right_head = head
            
            head = head.next
        
        left_head.next = rh.next
        right_head.next = None
        
        return lh.next
