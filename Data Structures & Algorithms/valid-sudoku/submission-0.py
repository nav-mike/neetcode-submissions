class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                # rows
                if val in rows[r]:
                    return False
                
                # columns
                if val in columns[c]:
                    return False
                
                # squares
                if val in squares[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(val)
                columns[c].add(val)
                squares[(r // 3, c // 3)].add(val)


        return True
            