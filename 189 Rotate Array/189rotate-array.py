class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0: return

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            return
    
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return

# Time: O(n + n) = O(n)
# Space: O(1)