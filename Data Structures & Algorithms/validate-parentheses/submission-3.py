class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        mapping = {')':'(','}':'{',']':'['}

        for ch in s:
            if ch in mapping:
                if not stack or mapping[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
        
        return not stack
