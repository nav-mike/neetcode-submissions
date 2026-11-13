class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            if (row, col) in path or min(row, col) < 0 or row >= rows or col >= cols or board[row][col] != word[index]:
                return False
            
            path.add((row, col))
            flag = (
                backtrack(row+1, col, index+1) or
                backtrack(row-1, col, index+1) or
                backtrack(row, col+1, index+1) or
                backtrack(row, col-1, index+1)
            )
            path.remove((row, col))

            return flag
        
        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, 0):
                    return True
        
        return False