class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num

        while l <= r:
            mid = (l + r) // 2
            curr_square = mid * mid
            if curr_square == num:
                return True
            elif curr_square < num:
                l = mid + 1
            else:
                r = mid - 1
        return False

# Time: O(log(num))
# Space: O(1)
            