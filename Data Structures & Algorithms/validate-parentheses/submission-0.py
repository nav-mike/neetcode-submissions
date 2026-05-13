class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for item in list(s):
            if self.isOpen(item):
                stack.append(item)
            elif len(stack) == 0:
                return False
            elif self.isOpen(stack[-1]):
                stack.pop(-1)
            else:
                return False

        return len(stack) == 0

    def isOpen(self, s: str) -> bool:
        return s == "[" or s == "{" or s == "("
