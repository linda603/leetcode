class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        line_sweep = [0] * (len(nums) + 1)

        for start, end in queries:
            line_sweep[start] += 1
            line_sweep[end + 1] -= 1
        
        count = 0
        for i, num in enumerate(nums):
            count += line_sweep[i]
            if count < num:
                return False
        return True
    
# Time: O(q + n)
# Space: O(n)