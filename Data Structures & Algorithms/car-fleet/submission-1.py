class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        for p, s in pairs:
            val = (target - p) / s
            if not stack or val > stack[-1]:
                stack.append(val)

        return len(stack)