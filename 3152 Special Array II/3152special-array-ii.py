class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] % 2 != nums[i - 1] % 2:
                prefix[i] = prefix[i - 1] + 1
        
        res = [True] * len(queries)
        for i, (l, r) in enumerate(queries):
            if prefix[r] - prefix[l] + 1 != (r - l + 1):
                res[i] = False
        return res

# Time: O(m + n). m: len(nums), n: len(queries)
# Space: O(m + n)