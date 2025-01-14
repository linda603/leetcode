class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        res = 1

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            curr_seq = 1
            while num + 1 in nums_set:
                curr_seq += 1
                num += 1
            res = max(res, curr_seq)
        return res

# Time: O(n + n)
# Space: O(n)