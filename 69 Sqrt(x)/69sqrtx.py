class Solution:
    def mySqrt(self, x: int) -> int:
        if not x: return 0
        for i in range(x + 1):
            if i * i <= x:
                res = i
            else:
                return res

# Time: O(n)
# Space: O(1)