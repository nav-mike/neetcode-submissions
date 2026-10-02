class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        letters = {}
        max_freq = 0
        left = 0
        for right in range(len(s)):
            letters[s[right]] = 1 + letters.get(s[right], 0)
            max_freq = max(max_freq, letters[s[right]])
            diff = right - left + 1 - max_freq
            if diff <= k:
                result = max(result, right - left + 1)
            else:
                letters[s[left]] -= 1
                left += 1

        return result