class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        chars = set()

        left = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            
            chars.add(s[right])
            result = max(result, len(chars))

        return result