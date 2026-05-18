class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = dict()

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        heap = []
        for key, value in hashMap.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for idx in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

        # for key, value in hashMap.items():
        #     result.append((key, value))

        # result = sorted(result, key=lambda item: -item[1])

        # return list(map(lambda item: item[0], result[:k]))
