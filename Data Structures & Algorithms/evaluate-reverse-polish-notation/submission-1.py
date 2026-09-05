class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b : a + b,
            "-": lambda a, b : a - b,
            "*": lambda a, b : a * b,
            "/": lambda a, b : a // b,
        }

        for token in tokens:
            if token.isnumeric():
                stack.append(token)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                result = str(ops[token](left, right))
                stack.append(result)
        
        return int(result)
