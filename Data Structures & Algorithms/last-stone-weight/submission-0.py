class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-item for item in stones]
        heapq.heapify(h)

        while len(h) > 1:
            x, y = -heapq.heappop(h), -heapq.heappop(h)
            if x == y:
                continue
            else:
                heapq.heappush(h, -abs(x - y))
        
        return -h[0] if len(h) == 1 else 0