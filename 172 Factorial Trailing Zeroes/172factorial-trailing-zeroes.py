class Solution:
    def trailingZeroes(self, n: int) -> int:
        # res = n / 5 + n / 5^2 + n / 5^3 + ...
        res = 0
        power_of_5 = 5
        while n >= power_of_5:
            res += n // power_of_5
            power_of_5 *= 5
        return res

#Time: O(log5(n))
#Space: O(1)