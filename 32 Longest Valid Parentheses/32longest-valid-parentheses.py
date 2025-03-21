class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                res = max(res, i - stack[-1])
        return res

# Time: O(n)
# Space: O(n)