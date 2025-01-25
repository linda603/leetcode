class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if not stack:
                    res += 1
                else:
                    stack.pop()
        return res + len(stack)

# Time: O(n)
# Space: O(n)