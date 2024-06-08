class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        res = 0

        while l <= r:
            mid = (l + r) // 2
            minCoins = (mid / 2) * (mid + 1)
            if minCoins <= n:
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res

#Time: O(nlogn)
#Space: O(1)