class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        res = ""
        # Check if result is negative
        if numerator * denominator < 0:
            res += "-"
        
        num = abs(numerator)
        den = abs(denominator)
        
        quotient = num // den
        remainder = num % den
        res += str(quotient)
        if remainder == 0:
            return res
        
        # in case remainder != 0, there is a fractional part
        res += "."

        pos_remainder = {} # map remainder: position
        while remainder != 0 and remainder not in pos_remainder:
            pos_remainder[remainder] = len(res)
            remainder *= 10
            res += str(remainder // den)
            remainder = remainder % den
        
        # Check if there is a repeating part
        if remainder in pos_remainder:
            res = res[:pos_remainder[remainder]] + "(" + res[pos_remainder[remainder]:] + ")"
        return res

# Time: O()
# Space: O()