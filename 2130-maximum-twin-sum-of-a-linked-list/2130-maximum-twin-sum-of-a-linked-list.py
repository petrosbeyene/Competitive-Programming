# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head) -> int:
        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next
        
        h_map = {}
        i = 0
        max_val = float('-inf')
        curr = head
        while curr:
            if i < l/2:
                h_map[i] = curr.val
            else:
                twin = l-i-1
                val = curr.val + h_map[twin]
                max_val = max(max_val, val)
            
            i += 1
            curr = curr.next
        
        return max_val if max_val != float('-inf') else 0
