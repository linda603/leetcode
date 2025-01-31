class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for num, cnt in count.items():
            if cnt > len(nums) / 3:
                res.append(num)
        return res

# Time: O(n + n)
# Space: O(n)