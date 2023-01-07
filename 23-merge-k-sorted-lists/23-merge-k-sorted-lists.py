# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        left = 0
        right = 1
        while right < len(lists):
            head1 = lists[left]
            head2 = lists[right]

            merged_list = self.mergeList(head1, head2)
            lists.pop(0)
            lists.pop(0)
            lists.insert(0, merged_list)
        
        return lists[0]
    
    def mergeList(self, head1, head2):
        dummy = tail = ListNode()
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
                tail = tail.next
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next
        if head1:
            tail.next = head1
        if head2:
            tail.next = head2
        
        return dummy.next
