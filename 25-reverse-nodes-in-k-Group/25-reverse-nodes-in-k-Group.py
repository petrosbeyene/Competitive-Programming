# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        groupPrev = dummy = ListNode(0, head)
        while True:
            Kth= self.getKthNode(groupPrev, k)
            if not Kth:
                break
            
            nextGroup = Kth.next
            prev, curr = Kth.next, groupPrev.next
            while curr != nextGroup:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = Kth
            groupPrev = temp
        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

