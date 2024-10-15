class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        
        return n & (n - 1) == 0

# Time: O(1)
# Space: O(1)