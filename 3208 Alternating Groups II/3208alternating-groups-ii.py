class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        count = 0
        l = 0

        for r in range(1, 2 * n):
            if colors[(r + n) % n] == colors[(r - 1 + n) % n]:
                l = r
            if l >= n:
                break
            if (l < r and (r - l + 1 == k)) or (r >= n and r + len(colors) - l == k):
                count += 1
                l += 1
        return count

# Time: O(2n)
# Space: O(1)