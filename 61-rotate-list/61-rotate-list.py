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
        dummy = ListNode(0, head)
        while head:
            if cnt == k+1:
                ans = temp = head.next
                head.next = None
                while temp and temp.next:
                    temp = temp.next
                
                if temp:
                    temp.next = dummy.next
                    return ans
                else:
                    return dummy.next
            
            head = head.next
            cnt -= 1
        
