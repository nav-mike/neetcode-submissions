class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, st = {}, {}

        for ch in s:
            ss[ch] = ss.get(ch, 0) + 1
        
        for ch in t:
            st[ch] = st.get(ch, 0) + 1
        
        return ss == st