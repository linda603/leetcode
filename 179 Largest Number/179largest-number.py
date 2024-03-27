class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        def largerNum(num1, num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1

        nums = sorted(nums, key = cmp_to_key(largerNum))
        return str(int("".join(nums)))
#Time: O(nlogn)
#Space: O(n) we allocate O(n) space for the final return string