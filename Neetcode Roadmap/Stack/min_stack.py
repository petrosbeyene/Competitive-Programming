class MinStack:

    def __init__(self):
        self.stack = []
        self.trackMinElement = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.trackMinElement or val <= self.trackMinElement[-1]:
            self.trackMinElement.append(val)

    def pop(self) -> None:
        curr = self.stack.pop()
        if curr == self.trackMinElement[-1]:
            self.trackMinElement.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.trackMinElement[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()