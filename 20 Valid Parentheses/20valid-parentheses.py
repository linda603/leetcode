class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack.pop() != mapping[c]:
                    return False
        return True if not stack else False

# Time: O(n)
# Space: O(n)

