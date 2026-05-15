class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return "".join(sorted(s)) == "".join(sorted(t))
        result = 0
        for ch in s:
            result ^= ord(ch)
        
        for ch in t:
            result ^= ord(ch)

        return result == 0