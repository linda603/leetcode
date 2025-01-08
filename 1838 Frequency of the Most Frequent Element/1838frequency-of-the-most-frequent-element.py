class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        total = 0

        l = 0
        for r in range(len(nums)):
            total += nums[r]
            # check if r - l + 1 is a valid window wtih freq of nums[r]
            if (r - l + 1) * nums[r] <= total + k:
                res = max(res, r - l + 1)
            else:
                total -= nums[l]
                l += 1
        return res

# Time: O(nlogn + n)
# Space: O(n)