class MinStack:

    def __init__(self):
        self.prefix = []
        self.stack = []


    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append(val)
            self.prefix.append(val)
        else:
            self.stack.append(val)
            self.prefix.append(min(self.prefix[-1],val))


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.prefix.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack:
            return self.prefix[-1]
        
