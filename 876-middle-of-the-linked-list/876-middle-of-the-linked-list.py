# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # h_list = []
        # while head != None:
        #     h_list.append(head)
        #     head = head.next
        # return h_list[len(h_list)//2]
        fast = slow = head
        while fast.next != None:
            slow = slow.next
            if fast.next.next != None:
                fast = fast.next.next
            else:
                return slow
        return slow
        
            
        