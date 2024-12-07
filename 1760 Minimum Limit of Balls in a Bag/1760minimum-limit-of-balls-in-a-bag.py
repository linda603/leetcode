class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)

        res = r

        while l <= r:
            mid = (l + r) // 2
            if self.valid(nums, maxOperations, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
    
    def valid(self, nums, operations, balls):
        needed_ops = 0

        for num in nums:
            needed_ops += math.ceil(num / balls) - 1
        return needed_ops <= operations

# Time: O(log(max(nums)))
# Space: O(1)
