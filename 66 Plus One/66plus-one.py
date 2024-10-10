class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            val = digits[i] + 1
            digits[i] = val % 10
            carry = val // 10
            if not carry:
                break
        if carry:
            digits = [1] + digits

        return digits

#Time: O(n)
#Space: O(1)