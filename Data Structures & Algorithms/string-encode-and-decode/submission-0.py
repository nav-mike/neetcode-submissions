class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = len(s)
            if length > 0:
                result = f"{result}{length}#{s}"

        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]

        result = []

        count = 0
        tmp = ""
        idx = 0

        while idx < len(s):
            if count == 0:
                if s[idx] != "#":
                    tmp += s[idx]
                else:
                    count = int(tmp)
                    tmp = ""
            else:
                tmp += s[idx]
                count -= 1
                if count == 0:
                    result.append(tmp)
                    tmp = ""
            idx += 1
        
        return result
