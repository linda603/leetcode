class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        stack = []

        for c in num:
            while stack and k and ord(stack[-1]) > ord(c):
                stack.pop()
                k -= 1
            stack.append(c)
        
        # if string vals are in non-decreasing order
        if k:
            stack = stack[:len(stack) - k]

        # remove leading zero
        start = 0
        while start < len(stack) and stack[start] == "0":
            start += 1
        res = "".join(stack[start:])

        return res if res else "0"

# Time: O(n)
# Space: O(n)