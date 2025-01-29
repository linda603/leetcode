class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # brute force
        res = float("inf")
        
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                if curr >= k:
                    res = min(res, j - i + 1)
        return res if res != float("inf") else -1

# Time: O(n^2)
# Space: O(1)