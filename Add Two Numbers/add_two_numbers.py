# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        while l1 != None:
            n1 += str(l1.val)
            l1 = l1.next
        n2 = ""
        while l2 != None:
            n2 += str(l2.val)
            l2 = l2.next
        
        n1 = n1[::-1]
        n2 = n2[::-1]
        result = int(n1) + int(n2)
        
        result = str(result)[::-1]
        
        temp = ListNode(0)
        head = temp
        for i in range(len(result)):
            temp.val = result[i]
            if i != len(result) -1:
                temp.next = ListNode(0)
            temp = temp.next
        
        return head
            