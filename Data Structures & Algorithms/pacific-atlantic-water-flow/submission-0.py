class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        result = []
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(row, col, ocean, prev_height):
            if (row not in range(rows) or
                col not in range(cols) or
                (row, col) in ocean or
                heights[row][col] < prev_height):
                return
            
            ocean.add((row, col))
            for dr, dc in ds:
                dfs(row+dr, col+dc, ocean, heights[row][col])
        
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows-1, col, atlantic, heights[rows-1][col])
        
        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols-1, atlantic, heights[row][cols-1])
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result