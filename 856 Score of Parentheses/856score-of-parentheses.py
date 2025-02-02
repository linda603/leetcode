class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for c in s:
            if c == "(":
                stack.append(-1) # -1 == "("
            else:
                if stack[-1] == -1:
                    stack.pop()
                    stack.append(1)
                else:
                    val = 0
                    while stack[-1] != -1:
                        val += stack.pop()
                    stack.pop()
                    stack.append(2 * val)
        return sum(stack)

# Time: O(n)
# Space: O(n)