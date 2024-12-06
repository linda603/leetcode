class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)

        total = 0
        cnt = 0
        for num in range(1, n + 1):
            if num not in banned:
                total += num
                if total > maxSum:
                    break
                cnt += 1
        return cnt

# Time: O(n)
# Space: O(n)