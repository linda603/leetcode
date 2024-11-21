class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.find_pal(s, i, i) # odd pals
            res += self.find_pal(s, i, i + 1) # even pals
        return res
    
    def find_pal(self, nums, l, r):
        if r >= len(nums): return 0
        res = 0

        while l >= 0 and r < len(nums) and nums[l] == nums[r]:
            res += 1
            l -= 1
            r += 1
        return res

# Time: O(n^2)
# Space: O(1)