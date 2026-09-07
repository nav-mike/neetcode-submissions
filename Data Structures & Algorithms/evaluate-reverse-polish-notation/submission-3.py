class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b : a + b,
            "-": lambda a, b : a - b, # btw reverse order
            "*": lambda a, b : a * b,
            "/": lambda a, b : int(float(a) / b) # reverse order as well
        }

        for token in tokens:
            if token in ops.keys():
                right = stack.pop()
                left = stack.pop()
                val = ops[token](left, right)
                stack.append(int(val))
            else:
                stack.append(int(token))

        return stack[0]