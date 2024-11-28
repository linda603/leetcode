class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += n % 2
            n = n // 2 # n >> 1
        return res

# Time: O(32)
# Space: O(1)