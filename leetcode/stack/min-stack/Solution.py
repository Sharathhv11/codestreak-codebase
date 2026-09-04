class MinStack:

    def __init__(self):
        
        self.stack: List[int] = list()
        self.minStack: List[int] = list()

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.minStack.append(min(value, self.minStack[-1] if len(self.minStack) != 0 else value + 1))


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()