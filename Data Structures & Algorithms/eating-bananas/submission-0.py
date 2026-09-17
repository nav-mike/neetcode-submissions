class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            k = (right + left) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            
            if total <= h:
                result = min(result, k)
                left = k + 1
            else:
                right = k - 1

        return result