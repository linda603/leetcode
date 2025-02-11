class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        stack = []

        for c in s:
            if stack and len(stack) >= n and "".join(stack[len(stack) - n:]) == part:
                cnt = n
                while cnt:
                    stack.pop()
                    cnt -= 1
            stack.append(c)
        if stack and len(stack) >= n and "".join(stack[len(stack) - n:]) == part:
            stack = stack[: len(stack) - n]
        return "".join(stack)

# Time: O(mn)
# Space: O(m + n)