class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
        return res

# Time: O(nlogn + n^2)
# Space: O(n)