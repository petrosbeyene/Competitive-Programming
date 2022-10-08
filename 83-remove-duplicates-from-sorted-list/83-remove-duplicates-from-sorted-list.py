# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        h_list = []
        while head:
            if head.val not in h_list:
                h_list.append(head.val)
            head = head.next
        
        res_head = temp = ListNode()
        for i in range(len(h_list)):
            temp.val = h_list[i]
            if i != len(h_list) -1:
                temp.next = ListNode()
            temp = temp.next
        return res_head