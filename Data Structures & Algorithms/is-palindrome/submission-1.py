class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        array = list(s.lower())

        while left < right:
            if not array[left].isalnum():
                left += 1
            elif not array[right].isalnum():
                right -= 1
            elif array[left] == array[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True