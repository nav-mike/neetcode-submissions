class Solution:
    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            length = len(s)
            parts.append(f"{length}#{s}")

        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            count = int(s[i:j])
            result.append(s[j + 1 : j + 1 + count])

            i = j + 1 + count

        return result
