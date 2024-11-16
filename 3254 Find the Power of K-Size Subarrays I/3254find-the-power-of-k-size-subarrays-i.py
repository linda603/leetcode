class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        for i in range(len(nums) - k + 1):
            power = -1 if k != 1 else nums[i]
            for j in range(i + 1, i + k):
                if nums[j - 1] + 1 != nums[j]:
                    break
                if j == i + k - 1:
                    power = nums[j]
            res.append(power)
        return res

# Time: O(nk)
# Space: O(n - k)