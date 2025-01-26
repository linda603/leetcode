class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # If val is a divisors of n then n // i also a divisor of n
        #
        # Divide all divisors of n into 2 parts:
        # 1. divisors smaller than sqrt(n)
        # 2. divisors bigger than sqrt(n)

        # Step 1: Check all possible num from 1 -> sqrt(n), if k == 0, return num
        # if sqrt(n) = integer. Ex: sqrt(4) = 2. We don't want to count 2 twice
        for val in range(1, math.ceil(sqrt(n))):
            if n % val == 0:
                k -= 1
            if k == 0:
                return val

        # Step 2: Check all possible num from n // (sqrt(n) -> 0), if k == 0, return num
        for val in range(int(sqrt(n)), 0, -1):
            if n % (n // val) == 0:
                k -= 1
                if k == 0:
                    return n // val
        return -1

# Time: O(2sqrt(n))
# Space: O(1)