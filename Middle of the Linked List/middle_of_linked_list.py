# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        h_list = []
        while head != None:
            h_list.append(head)
            head = head.next
        return h_list[len(h_list)//2]
        