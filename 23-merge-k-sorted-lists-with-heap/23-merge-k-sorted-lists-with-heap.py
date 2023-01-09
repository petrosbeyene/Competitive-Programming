# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        minHeap = []
        head = dummy = ListNode()
        for curr_node in lists:
            while curr_node:
                heapq.heappush(minHeap, curr_node.val)
                curr_node = curr_node.next
        
        while minHeap:
            val = heapq.heappop(minHeap)
            dummy.next = ListNode(val)
            dummy = dummy.next
        
        return head.next