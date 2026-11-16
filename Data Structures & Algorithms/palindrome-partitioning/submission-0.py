class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(i, subset):
            if i >= len(s):
                result.append(subset.copy())
                return
            
            for j in range(i, len(s)):
                if not self.is_palindrome(s, i, j):
                    continue
                
                subset.append(s[i:j+1])
                backtrack(j+1, subset)
                subset.pop()
        
        backtrack(0, [])

        return result
    
    def is_palindrome(self, string, left, right):
        while left < right:
            if string[left] != string[right]:
                return False
            
            left += 1
            right -= 1
        
        return True