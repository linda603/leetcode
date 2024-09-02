class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        digit_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        ten_map = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty", 
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        def get_string(n):
            # 123, 120, 102, 012, 100
            res = []

            hundred = n // 100 # 1
            if hundred:
                res.append(digit_map[hundred] + " Hundred")
            n = n % 100
            if n >= 20:
                ten = n // 10
                print("ten:", ten)
                one = n % 10
                if ten:
                    res.append(ten_map[ten * 10])
                if one:
                    res.append(digit_map[one])
            elif n: # in case 100, n now = 0, we don't wanna append 0 to res
                res.append(digit_map[n])
            return " ".join(res)

        big_string = ["", " Thousand", " Million", " Billion"]
        i = 0
        res = []
        
        while num:
            digits = num % 1000
            s = get_string(digits)
            if s: # in case num = 1.000.000.000
                res.append(s + big_string[i])
            num = num // 1000
            i += 1
        
        return " ".join(res[::-1])

#Time: O(log10(n)) = O(logn). n: how many digits in num, in this case 2^31 - 1 = 2.147.483.647 we have max 10 digits -> O(1)
#Space: O(1)