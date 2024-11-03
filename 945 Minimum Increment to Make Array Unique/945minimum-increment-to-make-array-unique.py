class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = collections.defaultdict(int)
        min_val = float("inf")
        max_val = float("-inf")

        for num in nums:
            count[num] += 1
            min_val = min(min_val, num)
            max_val = max(max_val, num)
        
        res = 0
        for key in range(min_val, len(nums) + max_val):
            # found duplicated num
            if count[key] > 1:
                extra = count[key] - 1
                count[key + 1] += extra
                res += extra
        return res

# Time: O(n + max_val)
# Space: O(n)
