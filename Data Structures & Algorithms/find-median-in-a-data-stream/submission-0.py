class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if self.right_heap and self.right_heap[0] < num:
            heapq.heappush(self.right_heap, num)
        else:
            heapq.heappush(self.left_heap, -num)

        if len(self.right_heap) > len(self.left_heap) + 1:
            val = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -val)
        elif len(self.left_heap) > len(self.right_heap) + 1:
            val = heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, -val)
        

    def findMedian(self) -> float:
        if len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0]
        elif len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        
        