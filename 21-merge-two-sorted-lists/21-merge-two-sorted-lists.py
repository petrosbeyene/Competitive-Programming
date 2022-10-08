# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        
        allvals = []
        while list1 != None:
            allvals.append(list1.val)
            list1 = list1.next
        
        while list2 != None:
            allvals.append(list2.val)
            list2 = list2.next
            
        allvals = sorted(allvals)
        
        temp = ListNode()
        head = temp
        
        for i in range(len(allvals)):
            temp.val = allvals[i]
            if i != len(allvals)-1:
                temp.next = ListNode()
            temp = temp.next
        return head
            
        