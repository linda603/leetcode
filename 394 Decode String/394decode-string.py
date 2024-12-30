class Solution:
    def decodeString(self, s: str) -> str:
        stack = [""]
        digits = "0123456789"
        val = 0

        for c in s:
            if c in digits:
                val = val * 10 + int(c)
            elif c == "[":
                stack.append(str(val))
                stack.append("")
                val = 0
            elif c == "]":
                str2 = stack.pop()
                cnt = int(stack.pop())
                str1 = stack.pop()
                stack.append(str1 + cnt * str2)
            else:
                stack[-1] += c
        return stack[0]

# Time: O(n)
# Space: O(n)