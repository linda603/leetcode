class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # nums = [0, 1, 1, 3]
        # curr = 0 ^ 1 ^ 1 =     0000
        # mask =.                0011
        # flip the last 00 from "0000" to 0011 by curr ^ mask
        res = []

        curr = 0
        for num in nums:
            curr ^= num

        mask = 2 ** maximumBit - 1
        for i in range(len(nums) - 1, -1, -1):
            res.append(curr ^ mask)
            curr = curr ^ nums[i]
        return res

# Time: O(n + n) = O(n)
# Space: O(1)