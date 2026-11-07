class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-count for count in counter.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1

            if not heap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append([count, time + n])
            
            if q and q[0][1] == time:
                count, _ = q.popleft()
                heapq.heappush(heap, count)

        return time