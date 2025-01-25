class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n = n // prime
                if n == 1:
                    return True
        return False

# Time: O(logn)
# Space: O(1)
            
