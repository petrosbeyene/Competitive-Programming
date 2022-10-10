# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pre = dummy = ListNode(0,head)
        while head and head.next:
            while head.next and head.val == head.next.val:
                head = head.next
            if pre.next == head:
                pre = pre.next
                
            else:
                pre.next = head.next
                
            head = head.next

        return dummy.next