class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = []

        while l <= r:
            val_l = nums[l] * nums[l]
            val_r = nums[r] * nums[r]
            if val_r >= val_l:
                res.append(val_r)
                r -= 1
            else:
                res.append(val_l)
                l += 1
        return res[::-1]

# Time: O(n)
# Space: O(1)