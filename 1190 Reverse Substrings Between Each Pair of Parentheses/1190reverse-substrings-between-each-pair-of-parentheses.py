class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ")":
                stack.append(c)
            else:
                substring = []
                while stack[-1] != "(":
                    top = stack.pop()
                    substring.append(top)
                stack.pop() #To remove "(" character
                stack.extend(substring)
        return "".join(stack)

#Time: O(n^2) worst case. Average O(n*m), n: len(s), m: longest substring
#Space: O(n)