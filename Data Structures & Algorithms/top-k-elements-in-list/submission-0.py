class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = dict()
        result = []

        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        for key, value in hashMap.items():
            result.append((key, value))

        result = sorted(result, key=lambda item: -item[1])

        return list(map(lambda item: item[0], result[:k]))
