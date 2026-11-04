class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for x, y in points:
            distance = x ** 2 + y ** 2
            heap.append([distance, x, y])
        
        heapq.heapify(heap)

        while heap and k > 0:
            _, x, y = heapq.heappop(heap)
            k -= 1
            result.append([x, y])
        
        return result