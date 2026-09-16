class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (h, i)

        for idx, height in enumerate(heights):
            index = idx
            while stack and stack[-1][0] >= height:
                h, i = stack.pop()
                val = h * (idx - i)
                max_area = max(val, max_area)
                index = i
            stack.append((height, index))
        
        for h, i in stack:
            val = h * (len(heights) - i)
            max_area = max(max_area, val)

        return max_area