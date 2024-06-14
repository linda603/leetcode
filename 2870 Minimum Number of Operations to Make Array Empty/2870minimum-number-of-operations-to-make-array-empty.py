class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        res = 0
        for num in count.values():
            if num == 1:
                return -1
            res += ceil(num / 3)
        return res

#Time: O(n)
#Space: O(n)