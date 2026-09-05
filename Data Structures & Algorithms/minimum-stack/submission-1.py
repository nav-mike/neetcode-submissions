from math import inf;

class MinStack:

    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        self.values.append(val)

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
        return self.values[-1]


    def getMin(self) -> int:
        result = self.values[0]

        for v in self.values:
            result = min(result, v)
        
        return result
