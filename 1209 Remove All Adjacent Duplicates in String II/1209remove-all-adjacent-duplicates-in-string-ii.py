class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [c, cnt]

        for c in s:
            if stack and stack[-1][0] == c:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([c, 1])
        
        res = ""
        for c, cnt in stack:
            res += c * cnt
        return res

# Time: O(2n + n) = O(n)
# Space: O(n)