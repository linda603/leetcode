class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        slow = n
        fast = n

        while True:
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(self.sum_of_squares(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
    
    def sum_of_squares(self, n):
        val = 0

        while n:
            digit = n % 10
            val += digit * digit
            n = n // 10
        return val

# Time: O(n)
# Space: O(1)