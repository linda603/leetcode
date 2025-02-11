class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s += "+"
        op = "+"
        val = 0

        for c in s:
            if c == " ":
                continue
            elif c.isdigit():
                val = val * 10 + int(c)
            else:
                if op == "+":
                    stack.append(val)
                elif op == "-":
                    stack.append(-val)
                elif op == "*":
                    prev = stack.pop()
                    stack.append(prev * val)
                elif op == "/":
                    prev = stack.pop()
                    stack.append(int(prev / val))
                op = c
                val = 0
        return sum(stack)

# Time: O(n)
# Space: O(n)