# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        cnt = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            cnt += 1
        

        k = k % cnt
        fast = slow = head
        
        dummy = ListNode(0, head)
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        
        ans = temp = slow.next
        slow.next = None
        
        while temp and temp.next:
            temp = temp.next
        
        if temp:
            temp.next = dummy.next
            return ans
        else:
            return dummy.next
        
        
