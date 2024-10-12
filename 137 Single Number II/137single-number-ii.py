class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        curr_bit = 0

        for shift in range(32):
            cnt = 0
            for num in nums:
                if (num >> shift) & 1: # to calculate how many 1 for bit 0, 1, 2, 3, ...
                    cnt += 1
            if cnt % 3:
                res = res | (1 << shift)
        
        # negative number
        if res >= (1 << 31):
            res = res - (1 << 32)

        return res

# Time: O(32n)
# Space: O(1)