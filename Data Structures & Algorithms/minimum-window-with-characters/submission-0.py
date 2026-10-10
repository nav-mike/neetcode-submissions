class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count, window = {}, {}

        for ch in t:
            t_count[ch] = 1 + t_count.get(ch, 0)
        
        have, need = 0, len(t_count)
        i, j, length = -1, -1, len(s) + 10

        left = 0
        for right in range(len(s)):
            ch = s[right]

            if ch in t_count:
                window[ch] = 1 + window.get(ch, 0)

                if window[ch] == t_count[ch]:
                    have += 1
                
            while have == need:
                if length > right - left + 1:
                    length = right - left + 1
                    i, j = left, right

                ch = s[left]

                if ch in t_count:
                    if window[ch] == t_count[ch]:
                        have -= 1

                    window[ch] -= 1
                left += 1

        return s[i:j+1] if length != len(s) + 10 else ""