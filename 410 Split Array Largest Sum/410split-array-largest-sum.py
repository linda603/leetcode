class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l <= r:
            mid = (l + r) // 2
            if self.can_split(nums, k, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
    
    def can_split(self, nums, k, largest):
        cnt = 1
        curr_sum = 0

        for num in nums:
            if curr_sum + num > largest:
                cnt += 1
                curr_sum = 0
            curr_sum += num
        return cnt <= k

# Time: O(log(sum(nums)) * n)
# Space: O(1)