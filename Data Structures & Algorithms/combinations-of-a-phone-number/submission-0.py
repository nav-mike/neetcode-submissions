class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def backtrack(index, s):
            if len(s) == len(digits):
                result.append("".join(s))
                return
            
            for ch in d[digits[index]]:
                s.append(ch)
                backtrack(index+1, s)
                s.pop()
        
        if digits:
            backtrack(0, [])

        return result