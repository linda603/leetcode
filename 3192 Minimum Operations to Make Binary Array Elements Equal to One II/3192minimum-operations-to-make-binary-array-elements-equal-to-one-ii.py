class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = False
        res = 0
        pending = False
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0 and not pending:
                if prev:
                    res += 2
                    pending = True
                else:
                    res += 1
                    pending = True
            if nums[i] == 1:
                pending = False
                prev = True
        return res