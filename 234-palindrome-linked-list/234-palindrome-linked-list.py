# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        curr = head
        ls = []
        while curr:
            ls.append(curr.val)
            curr = curr.next
        return ls == ls[::-1]
        