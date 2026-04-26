class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.min:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)
        
    def pop(self) -> None:
        result = self.stack.pop()
        
        if self.min and result == self.min[-1]:
            self.min.pop()
        return result

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min[-1] if self.min else None