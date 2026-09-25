class TimeMap:

    def __init__(self):
        self.values: dict[str, tuple(str, int)] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        
        self.values[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""

        result = ""
        left, right = 0, len(self.values[key]) - 1

        while left <= right:
            mid = (left + right) // 2
            result = self.values[key][mid][0]
            if self.values[key][mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return result
        
