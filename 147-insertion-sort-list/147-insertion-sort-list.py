# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #create array of head values
        array = []
        while head != None:
            array.append(head.val)
            head = head.next
        
        #sort the array using insertion sort
        for i in range(1, len(array)):
                key = array[i]
                j = i - 1       
                
                while j >= 0 and key < array[j]:
                    array[j + 1] = array[j]
                    j = j - 1
        
                array[j + 1] = key
        
        #change the sorted array back to linked list
        dummyHead = temp = ListNode()
        for i in range(len(array)):
            temp.val = array[i]
            if i != len(array) -1:
                temp.next = ListNode()
            temp = temp.next
        
        return dummyHead