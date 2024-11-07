class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0

        for i in range(32):
            cnt = 0
            for num in candidates:
                if (1 << i) & num:
                    cnt += 1
            res = max(res, cnt)
        return res

# Time: O(32*n)
# Space: O(1) = O(1)