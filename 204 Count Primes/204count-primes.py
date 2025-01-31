class Solution:
    def countPrimes(self, n: int) -> int:
        seen = [0] * n
        res = 0

        for i in range(2, n):
            if seen[i]:
                continue
            res += 1
            j = i
            while i * j < n:
                seen[i * j] = 1 # not a prime number
                j += 1
        return res

# Time: O(n)
# Space: O(n)