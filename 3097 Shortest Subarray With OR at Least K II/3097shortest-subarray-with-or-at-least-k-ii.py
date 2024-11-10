class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = float("inf") # min_length
        bits = [0] * 32

        def update_bits(bits, num, diff):
            for i in range(32):
                if num & (1 << i):
                    bits[i] += diff

        l = 0
        total = 0
        for r in range(n):
            update_bits(bits, nums[r], 1)
            while l <= r and self.convert_bits(bits) >= k:
                res = min(res, r - l + 1)
                update_bits(bits, nums[l], -1)
                l += 1
                
        return res if res != float("inf") else -1
    
    # convert bits to number
    def convert_bits(self, bits):
        res = 0

        for i in range(32):
            if bits[i]:
                res += (1 << i)
        return res

# Time: O(n)
# Space: O(1)