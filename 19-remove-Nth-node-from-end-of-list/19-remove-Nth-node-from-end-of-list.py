# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1

        if length == 1:
            return None

        if length - n == 0:
            head = head.next
            return head
        
        index = length - n
        curr = head
        for _ in range(index-1):
            curr = curr.next

        if curr.next and curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return head