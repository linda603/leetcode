class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        if total == 0: return 0
        curr_one = 0
        res = float("inf")

        l = 0
        for r in range(2 * len(nums)):
            if nums[r % n]:
                curr_one += 1
            if l <= r and r - l + 1 == total:
                res = min(res, r - l + 1 - curr_one)
                if nums[l % n]:
                    curr_one -= 1
                l += 1

            elif l > r and r + n - l == total:
                res = min(res, r + n - l - curr_one)
                if nums[l % n]:
                    curr_one -= 1
                l += 1
        return res

        