class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min[-1]:
            self.min.pop()

    def top(self) -> int | None:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int | None:
        return self.min[-1] if self.min else None