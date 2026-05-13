class Solution:
    LETTERS = 'qwertyuiopasdfghjklzxcvbnm'

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        array = list(s.lower())

        while left < right:
            if array[left] not in self.LETTERS:
                left += 1
            elif array[right] not in self.LETTERS:
                right -= 1
            elif array[left] == array[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True