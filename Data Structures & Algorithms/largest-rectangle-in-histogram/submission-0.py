class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prefixes, suffixes = [0] * n, [0] * n
        result = 0

        for idx in range(1, n):
            prefixes[idx] = min(prefixes[idx-1], heights[idx])

        return result
        