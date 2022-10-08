# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        val_list = []
        while head != None:
            val_list.append(head)
            head = head.next
        return val_list[len(val_list)//2]
        