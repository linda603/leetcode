class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += count.get(key, 0)
            count[key] = 1 + count.get(key, 0)

        return (n * (n - 1)) // 2 - good_pairs

# Time: O(n)
# Space: O(n)