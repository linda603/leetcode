class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0 # max sum
        curr_sum = 0
        seen = set()

        l = 0
        for r in range(len(nums)):
            while nums[r] in seen or r - l + 1 > k:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            seen.add(nums[r])
            curr_sum += nums[r]

            if r - l + 1 == k:
                res = max(res, curr_sum)
        return res

# Time: O(n)
# Space: O(k)