class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        result = self.stack[0]

        for idx in range(1, len(self.stack)):
            if self.stack[idx] < result:
                result = self.stack[idx]

        return result
