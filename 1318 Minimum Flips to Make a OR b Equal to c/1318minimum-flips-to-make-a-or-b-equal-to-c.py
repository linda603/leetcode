class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0

        while a or b or c:
            bitA = a & 1
            bitB = b & 1
            bitC = c & 1

            if bitC == 1:
                if bitA == 0 and bitB == 0:
                    res += 1
            else:
                res += bitA + bitB
            a >>= 1
            b >>= 1
            c >>= 1
        return res

#Time: O(n) n: number of bits
#Space: O(1)

# what if a = 1, b = 1, c = 2, res = 3??