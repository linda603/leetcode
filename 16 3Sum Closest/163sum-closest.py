class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        closet = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total
                if abs(total - target) < abs(closet - target):
                    closet = total
                if total < target:
                    l += 1
                else:
                    r -= 1
        return closet

#Time: O(nlogn + n^2) =O(n^2)
#Space: O(n)