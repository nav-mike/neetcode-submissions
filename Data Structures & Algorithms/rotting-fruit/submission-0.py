class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        fresh = 0
        time = 0
        q = collections.deque()
        ds = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def process(row, col):
            nonlocal fresh
            if (row not in range(rows) or
                col not in range(cols) or
                (row, col) in visited or
                grid[row][col] != 1):
                return
            
            visited.add((row, col))
            fresh -= 1
            q.append((row, col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    visited.add((row, col))
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        while fresh > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in ds:
                    process(row+dr, col+dc)
            time += 1
        

        return time if fresh == 0 else -1