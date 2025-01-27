class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        cache = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            score_taking_left = nums[l] - dfs(l + 1, r)
            score_taking_right = nums[r] - dfs(l, r - 1)
            cache[(l, r)] = max(score_taking_left, score_taking_right)
            return cache[(l, r)]
        return dfs(0, len(nums) - 1) >= 0

# Time: O(2^n) -> O(n^2)
# Space: O(n^2)