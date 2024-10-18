class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                new_target = target - nums[i] - nums[j]
                l = j + 1
                r = len(nums) - 1
                
                while l < r:
                    curr = nums[l] + nums[r]
                    if curr == new_target:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif curr < new_target:
                        l += 1
                    else:
                        r -= 1
        return [val for val in res]

# Time: O(nlogn + n^3) = O(n^3)
# Space: O(n) due to sorting - without res space