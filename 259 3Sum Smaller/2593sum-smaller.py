class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum < target:
                    # [1, 2, 3, 5, 8] target = 9
                    #. i. l.    r
                    # curr_sum = 1 + 2 + 5 = 8 < 9 -> there are 3 pairs l, r sastified
                    # (2, 5), (2, 4), (2, 3) starting from left
                    res += r - l 
                    l += 1
                else:
                    r -= 1
        return res

# Time: O(nlogn + n^2)
# Space: O(n)