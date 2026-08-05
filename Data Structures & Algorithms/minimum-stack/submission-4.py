class MinStack:

    def __init__(self):
        self.stack = []
        self.lowest_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.lowest_stack[-1] if self.lowest_stack else val)
        self.lowest_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.lowest_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.lowest_stack[-1]
