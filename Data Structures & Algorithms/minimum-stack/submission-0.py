class MinStack:

    def __init__(self):
        self.minStack = [] # (currMin, ind)
        self.stack = [] # (val, ind)
        self.ind = 0

    def push(self, val: int) -> None:
        self.stack.append((val, self.ind))
        if len(self.minStack) > 0:
            currMin, _ = self.minStack[-1]
            if val < currMin:
                self.minStack.append((val, self.ind))
        else:
            self.minStack.append((val, self.ind))
        self.ind += 1

    def pop(self) -> None:
        _, ind = self.stack.pop()
        if len(self.minStack) > 0 and self.minStack[-1][1] == ind:
            self.minStack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1][0]
        return None
