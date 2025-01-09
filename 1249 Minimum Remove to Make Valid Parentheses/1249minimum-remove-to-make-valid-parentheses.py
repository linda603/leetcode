class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        arr = list(s)
        stack = []

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    arr[i] = ""
        
        while stack:
            arr[stack.pop()] = ""
        return "".join(arr)

# Time: O(n)
# Space: O(n) due to arr + stack