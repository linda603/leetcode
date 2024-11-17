class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cnt = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                if cnt > res:
                    res = cnt
            else:
                cnt = 0
        return res

# Time: O(n)
# Space: O(1)