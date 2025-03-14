class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k: return 0
        if k == 1: return max(candies)

        def is_valid(pos_candy):
            count = 0

            for candy in candies:
                count += candy // pos_candy # 1 pile can give to multiple children
            return count >= k

        l = 1
        r = max(candies)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if is_valid(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
# Time: O(log(max(candies))*n)
# Space: O(1)