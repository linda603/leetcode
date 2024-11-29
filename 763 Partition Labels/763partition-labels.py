class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_map = {c: i for i, c in enumerate(s)}
        res = []
        left, right = 0, 0

        for i, c in enumerate(s):
            right = max(right, idx_map[c])
            if i == right:
                res.append(right - left + 1)
                left = right + 1
        return res

# Time: O(2n)
# Space: O(26) = O(1)