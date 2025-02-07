class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        cnt = 1

        for i in range(2 * n):
            if nums[i % n] >= nums[(i - 1) % n]:
                cnt += 1
                if cnt == n:
                    return True
            else:
                cnt = 1
        return cnt == n

# Time: O(2n)
# Space: O(1)