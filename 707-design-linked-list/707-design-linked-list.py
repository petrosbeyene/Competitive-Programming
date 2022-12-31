class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.dummy_node = Node(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        curr = self.dummy_node
        for _ in range(index):
            curr = curr.next
        return curr.next.data

    def addAtHead(self, val: int) -> None:
        temp = self.dummy_node.next
        self.dummy_node.next = Node(val)
        self.dummy_node.next.next = temp
        self.length += 1

    def addAtTail(self, val: int) -> None:
        curr = self.dummy_node
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        curr = self.dummy_node
        for _ in range(index):
            curr = curr.next
        temp = curr.next
        curr.next = Node(val)
        curr.next.next = temp
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        curr = self.dummy_node
        for _ in range(index):
            curr = curr.next
        temp = curr.next
        curr.next = temp.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)