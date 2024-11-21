class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        half = total // 2 # half
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            tmp = dp.copy()
            for curr_sum in dp:
                if curr_sum + nums[i] == half:
                    return True
                if curr_sum + nums[i] < half:
                    tmp.add(curr_sum + nums[i])
            dp = tmp
        return False

# Time: O(n*half)
# Space: O(half)
