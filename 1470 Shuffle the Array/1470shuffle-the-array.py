class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        for i in range(len(nums) - n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res

# Time: O(n)
# Space: O(n)