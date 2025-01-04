class Solution:
    def addDigits(self, num: int) -> int:
        
        while num // 10 > 0:
            curr = 0
            while num:
                curr += num % 10
                num = num // 10
            num = curr
        return num

# Time: O(1)
# Space: O(1)