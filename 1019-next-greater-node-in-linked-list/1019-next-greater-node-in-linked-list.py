# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        dummyHead = head
        while dummyHead:
            ans.append(0)
            dummyHead = dummyHead.next
        
        i = 0
        stack = []
        while head:
            while stack and head.val > stack[-1][1]:
                idx = stack.pop()[0]
                ans[idx] = head.val
            stack.append([i, head.val])
            head = head.next
            i += 1
        return ans
        
        
#         d = {}
#         dummyHead = trav = head
#         while dummyHead != None:
#             d[dummyHead.val] = 0
#             dummyHead = dummyHead.next
        
#         stack = []
#         while trav != None:
#             while stack and trav.val > stack[-1]:
#                 val = stack.pop()
#                 d[val] = trav.val
#             stack.append(trav.val)
#             trav = trav.next
        
#         answer = []
#         while head != None:
#             answer.append(d[head.val])
#             head = head.next
        
#         return answer
        
            
        
        
        