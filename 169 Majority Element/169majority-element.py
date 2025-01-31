class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for num, cnt in count.items():
            if cnt > len(nums) / 2:
                res = num
        return res

# Time: O(n)
# Space: O(n)